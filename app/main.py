from fastapi import FastAPI
from app.routes import product, order

app = FastAPI()

# Include the product and order routers
app.include_router(product.router)  
app.include_router(order.router) 