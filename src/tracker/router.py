from fastapi import FastAPI, APIRouter, Depends
from .dtos import TransactionDTO, UpdateTransactionDTO
from src.tracker import controller
from src.user.auth import get_current_user

router = APIRouter(prefix="/tracker", tags=["Tracker"])

@router.post("/add")
def add(txn : TransactionDTO, user=Depends(get_current_user)):
    return controller.create_transaction(txn.dict(), user)

@router.get("/all")
def get_all_transaction(user=Depends(get_current_user)):
    return controller.get_all_transaction(user)

@router.get("/all/{id}")
def get_one_transaction(id : str, user=Depends(get_current_user)):
    return controller.get_one_transaction(id, user)

@router.put("/update/{id}")
def update(id: str, txn: UpdateTransactionDTO, user=Depends(get_current_user)):
    return controller.update_transaction(id, txn.dict(exclude_none=True), user)


@router.delete("/delete/{id}")
def update(id: str):
    return controller.delete_transaction(id)


@router.get("/balance")
def get_balance():
    return controller.calculate_balance()


@router.get("/filter/{type}")
def filter_transactions(type : str):
    return controller.filter_transactions(type)


@router.get("/monthly")
def get_monthly(user=Depends(get_current_user)):
    return controller.monthly_summary(user)


@router.get("/yearly")
def get_yearly(user=Depends(get_current_user)):
    return controller.yearly_summary(user)


@router.get("/quaterly")
def get_quaterly(user=Depends(get_current_user)):
    return controller.quaterly_summary(user)


@router.get("/check/{id}")
def check(id : str):
    return controller.check_transaction_exits(id)