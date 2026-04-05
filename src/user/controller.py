from src.utils.db import database
from fastapi import HTTPException
from bson import ObjectId
from datetime import datetime, timedelta, timezone
import secrets
import hashlib
from src.user.auth import hash_password, verify_password, create_access_token, create_refresh_token, verify_refresh_token, ACCESS_TOKEN_EXPIRE_MINUTES

users_collection = database.users


# ***** Refresh Token
def refresh_token(token: str):
    user_data = verify_refresh_token(token)
    new_access_token = create_access_token({"user_id": user_data["user_id"]}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": new_access_token, "token_type": "bearer"}

# **** Register
def register_user(data):
    existing = users_collection.find_one({
        "$or": [{"email": data["email"].lower()}, {"name": data["name"]}]
    })
    if existing:
        raise HTTPException(400, "User already exist")
    
    data["password"] = hash_password(data["password"])

    new_user = users_collection.insert_one(data)

    return {"message" : "User Created Sucessfully...!!", "id" : str(new_user.inserted_id)}
    

# ***** Login with jwt
def login_user(data : dict):

        user = users_collection.find_one({"email" : data["email"].lower()})
        if not user:
            raise HTTPException(404, "User not found")
    
        if not verify_password(data["password"], user["password"]):
            raise HTTPException(401, "Invalid credentials")
    
        token = create_access_token({"user_id": str(user["_id"])}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        refresh_token = create_refresh_token({"user_id": str(user["_id"])})

        return {
            "access_token": token,
            "refresh_token": refresh_token,
            "name": user["name"],
            "token_type": "bearer"
        }


# ***** Forget Password
def forgot_password(email : str):
    email = email.lower()
    user = users_collection.find_one({"email" : email})
    if not user:
        raise HTTPException(404, "User not found")
    
    # token = secrets.token_hex(16)
    token = secrets.token_hex(16)
    hashed_token = hashlib.sha256(token.encode()).hexdigest()

    expiry = datetime.now(timezone.utc) + timedelta(minutes=15)

    users_collection.update_one(
        {"_id": user["_id"]},
        {"$set" : {"reset_token" : hashed_token, "reset_expiry" : expiry}}
    )

    return {"message" : "Reset Token Generated", "token" : token}


# ***** Reset Password
def reset_password(token : str, new_password : str):

    hashed_token = hashlib.sha256(token.encode()).hexdigest()

    user = users_collection.find_one({"reset_token" : hashed_token})
    if not user:
        raise HTTPException(400, "Invalid Token")
    
    expiry = user["reset_expiry"]

    if expiry.tzinfo is None:
        expiry = expiry.replace(tzinfo=timezone.utc)

    if expiry < datetime.now(timezone.utc):
        raise HTTPException(400, "Token Expired")
    
    # if user["reset_expiry"] < datetime.now(timezone.utc):
    #     raise HTTPException(400, "Token Expired")
    
    users_collection.update_one(
        {"_id" : user["_id"]},
        {
            "$set": {"password": hash_password(new_password)},
            "$unset" : {"reset_token" : "", "reset_expiry" : ""}
        }
    )

    return {"message" : "Password updated Successfully...!!!"}




    

