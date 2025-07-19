from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    productId: str
    qty: int

class OrderCreate(BaseModel):
    userId: str
    items: List[OrderItem]

class OrderOutItem(BaseModel):
    productDetails: dict
    qty: int

class OrderOut(BaseModel):
    id: str
    items: List[OrderOutItem]
    total: float
