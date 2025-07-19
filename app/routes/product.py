from fastapi import APIRouter
from app.db import db
from app.schemas.product import ProductCreate

router = APIRouter()

@router.post("/products", status_code=201)
async def create_product(product: ProductCreate):
    result = await db.products.insert_one(product.dict())
    return {"id": str(result.inserted_id)}