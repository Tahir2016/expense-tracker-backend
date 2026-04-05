from pydantic import BaseModel, Field
from datetime import datetime

class TransactionDTO(BaseModel):
    title : str
    amount : float
    type : str
    category : str
    created_at: datetime = Field(default_factory=datetime.now)

class UpdateTransactionDTO(BaseModel):
    title: str | None = None
    amount: float | None = None
    type: str | None = None
    category: str | None = None

    
