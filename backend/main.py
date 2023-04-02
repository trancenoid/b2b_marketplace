# Main file to run the FastAPI application
from fastapi import FastAPI

from app.database.session import engine
from app.database.base import Base
from app.auth.routes import auth_router
from app.products.routes import products_router
from app.orders.routes import orders_router


app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Mount the authentication routes
app.include_router(auth_router)

# Mount the product routes
app.include_router(products_router, prefix="/products")

# Mount the order routes
app.include_router(orders_router, prefix="/orders")