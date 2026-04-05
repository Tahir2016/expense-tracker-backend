
from pydantic import BaseModel, EmailStr

class UserRegisterDTO(BaseModel):
    name : str
    email : EmailStr
    password : str

class UserLoginDTO(BaseModel):
    email : EmailStr
    password : str

class ForgotPasswordDTO(BaseModel):
    email: EmailStr

class ResetPasswordDTO(BaseModel):
    token : str
    new_password : str

class RefreshTokenDTO(BaseModel):
    refresh_token: str