from fastapi import APIRouter
from src.user.dtos import UserRegisterDTO, UserLoginDTO, ResetPasswordDTO, ForgotPasswordDTO, RefreshTokenDTO
from src.user import controller

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register")
def register_user(user : UserRegisterDTO):
    return controller.register_user(user.dict())


@router.post("/login")
def login_user(user : UserLoginDTO):
    return controller.login_user(user.dict())


@router.post("/refresh")
def refresh_token(data: RefreshTokenDTO):
    return controller.refresh_token(data.refresh_token)


@router.post("/forgot-password")
def forgot_password(data : ForgotPasswordDTO):
    return controller.forgot_password(data.email)


@router.put("/reset-password")
def reset_password(data : ResetPasswordDTO):
    return controller.reset_password(data.token, data.new_password)