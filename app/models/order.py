def orderModel(order: dict):
    return {
        "id": str(order["_id"]),
        "userId": order["userId"],
        "items": order["items"]
    }
