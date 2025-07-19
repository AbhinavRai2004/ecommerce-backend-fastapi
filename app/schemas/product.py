from pydantic import BaseModel
from typing import List

class SizeEntry(BaseModel):
    size: str
    quantity: int

class ProductCreate(BaseModel):
    name: str
    price: float
    sizes: List[SizeEntry]

class ProductOut(BaseModel):
    id: str
