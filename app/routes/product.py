from fastapi import APIRouter, Query
from typing import Optional, List
from app.db import db
from app.schemas.product import ProductCreate, ProductOut
from app.models.product import productModel

router = APIRouter()

@router.post("/products", status_code=201)
async def create_product(product: ProductCreate):
    result = await db.products.insert_one(product.dict())
    return {"id": str(result.inserted_id)}

@router.get("/products", status_code=200)
async def list_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}

    if size:
        query["sizes.size"] = size

    total = await db.products.count_documents(query)
    cursor = db.products.find(query).skip(offset).limit(limit)
    products = await cursor.to_list(length=limit)

    return {
        "data": [productModel(p) for p in products],
        "page": {
            "next": offset + limit if offset + limit < total else None,
            "limit": limit,
            "previous": max(offset - limit, 0) if offset > 0 else None
        }
    }