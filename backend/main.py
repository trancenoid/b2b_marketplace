from fastapi import FastAPI
from api.auth.auth_routes import auth_router
from api.orders.order_routes import order_router
from api.products.product_routes import product_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(product_router)
app.include_router(order_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)