from fastapi import APIRouter, Query
from typing import Optional, List
from app.db import db
from app.schemas.product import ProductCreate, ProductOut
from app.models.product import productModel

router = APIRouter()

# Endpoint to create a new product
@router.post("/products", status_code=201)
async def createProduct(product: ProductCreate):
    result = await db.products.insert_one(product.dict())
    return {"id": str(result.inserted_id)}

# Endpoint to get products with optional filters
@router.get("/products", status_code=200)
async def getProducts(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}

    # Apply filters if provided
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size

    total = await db.products.count_documents(query)
    if total == 0:
        return {
            "data": [],
            "page": {
                "next": 0,
                "limit": limit,
                "previous": 0,
            }
    }
    
    cursor = db.products.find(query).skip(offset).limit(limit)
    products = await cursor.to_list(length=limit)

    # Pagination logic
    return {
         "data": [productModel(p) for p in products],
        "page": {
            "next": offset + limit if offset + limit > total else 10,
            "limit": limit,
            "previous": offset - limit,
        }
    }



