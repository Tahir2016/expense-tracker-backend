from src.utils.db import collection
from .models import transaction_entity, transactions_entity
from bson import ObjectId
from datetime import datetime
from bson.errors import InvalidId
from fastapi import HTTPException

def create_transaction(data, user):
    data["user_id"] = user["user_id"]
    result = collection.insert_one(data)
    new_txn = collection.find_one({"_id":result.inserted_id})
    return transaction_entity(new_txn)


def get_all_transaction(user):
    txns = []
    for txn in collection.find({"user_id" : user["user_id"]}):
        txns.append(transaction_entity(txn))
    return txns


def update_transaction(id: str, data: dict, user):
    if not ObjectId.is_valid(id):
        return {"error" : "Invalid Id"}
    
    data.pop("user_id", None)
    
    result = collection.update_one(
        {"_id": ObjectId(id),
         "user_id": user["user_id"]},
        {"$set": data}
    )

    if result.matched_count == 0:
        return {"error": "Transaction not found or unauthorized"}
    
    return {"message" : "Transaction updated Successfully...!!", "data" : data}


def get_one_transaction(id : str, user):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    
    obj_id = ObjectId(id)

    txn = collection.find_one({"_id" : obj_id, "user_id": user["user_id"]})

    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    return {
    "message": "Transaction fetched successfully", "data": transaction_entity(txn)}


def delete_transaction(id: str):
    if not ObjectId.is_valid(id):
        return {"error" : "Invalid Id"}
    
    result = collection.delete_one(
        {"_id": ObjectId(id)},
    )

    if result.deleted_count == 0:
        return {"error": "Transaction not found"}

    return {"message" : "Transaction Deleted Successfully...!!"}
    

def calculate_balance():
    total_income = 0
    total_expense = 0

    for txn in collection.find():
        if txn["type"] == "income":
            total_income += txn["amount"]
        else:
            total_expense += txn["amount"]

    balance = total_income - total_expense

    return {
        "total_income" : total_income,
        "total_expense" : total_expense,
        "balance" : balance
    }


def filter_transactions(type : str):
    txns = []
    for txn in collection.find({type : str}):
        txns.append(txn)
    return txns


def category_summary():
    data = {}

    for txn in collection.find():
        cat = txn["category"]
        data[cat] = data.get(cat, 0) + txn["amount"]

    return data


def recent_transaction():
    txns = []
    for txn in collection.find().sort("_id", -1).limit(5):
        txns.append(txn)
    return txns


def monthly_summary(user):
    data = {}
    for txn in collection.find({"user_id": user["user_id"]}):
        month = txn.get("created_at", datetime.now()).strftime("%B %Y")
        if month not in data:
            data[month] = {"income": 0, "expense": 0, "transactions": []}
        if txn["type"] == "income":
            data[month]["income"] += txn["amount"]
        else:
            data[month]["expense"] += txn["amount"]
        data[month]["transactions"].append(transaction_entity(txn))
    return data


def yearly_summary(user):
    data = {}
    for txn in collection.find({"user_id": user["user_id"]}):
        year = str(txn.get("created_at", datetime.now()).year)
        if year not in data:
            data[year] = {"income": 0, "expense": 0, "transactions": []}
        if txn["type"] == "income":
            data[year]["income"] += txn["amount"]
        else:
            data[year]["expense"] += txn["amount"]
        data[year]["transactions"].append(transaction_entity(txn))
    return data


def quaterly_summary(user):
    data = {
        "Q1": {"income": 0, "expense": 0, "transactions": []},
        "Q2": {"income": 0, "expense": 0, "transactions": []},
        "Q3": {"income": 0, "expense": 0, "transactions": []},
        "Q4": {"income": 0, "expense": 0, "transactions": []},
    }
    for txn in collection.find({"user_id": user["user_id"]}):
        month = txn.get("created_at", datetime.now()).month
        if month <= 3:
            q = "Q1"
        elif month <= 6:
            q = "Q2"
        elif month <= 9:
            q = "Q3"
        else:
            q = "Q4"
        if txn["type"] == "income":
            data[q]["income"] += txn["amount"]
        else:
            data[q]["expense"] += txn["amount"]
        data[q]["transactions"].append(transaction_entity(txn))
    return data


def check_transaction_exits(id :str):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        return {"error" : "Invalid ID Format"}
    
    txn = collection.find_one({"_id" : obj_id})
    if txn:
        return{"exists" : True}
    return{"exists" : False}
