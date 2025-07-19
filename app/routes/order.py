from fastapi import APIRouter
from bson import ObjectId

from app.db import db
from app.schemas.order import OrderCreate


router = APIRouter()

@router.post("/orders", status_code=201)
async def createOrder(order: OrderCreate):
    result = await db.orders.insert_one(order.dict())
    return {"id": str(result.inserted_id)}

@router.get("/orders/{user_id}")
async def getOrders(user_id: str, limit: int = 10, offset: int = 0):
    query = {"userId": user_id}
    total = await db.orders.count_documents(query)
    cursor = db.orders.find(query).skip(offset).limit(limit)
    orders = await cursor.to_list(length=limit)

    data = []
    for order in orders:
        enriched_items = []
        total_price = 0
        for item in order["items"]:
            product = await db.products.find_one({"_id": ObjectId(item["productId"])})
            if product:
                product_info = {
                    "name": product["name"],
                    "price": product["price"]
                }
                item_total = product["price"] * item["qty"]
                total_price += item_total

                enriched_items.append({
                    "productDetails": product_info,
                    "qty": item["qty"]
                })

        data.append({
            "id": str(order["_id"]),
            "items": enriched_items,
            "total": round(total_price, 2)
        })

    return {
        "data": data,
        "page": {
            "limit": limit,
            "next": offset + limit if offset + limit < total else None,
            "previous": max(offset - limit, 0) if offset > 0 else None
        }
    }
