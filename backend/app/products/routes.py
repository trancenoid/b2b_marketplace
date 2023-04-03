# Contains routes for products
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.routes import get_current_user
from app.database import get_session
from app.database import crud
from app import schemas

products_router = APIRouter()

@products_router.get("/products")
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products

@products_router.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_session)):
    product = crud.get_product(db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@products_router.post("/products")
def create_product(product: schemas.ProductCreate, current_user : schemas.User = Depends(get_current_user), 
                   db: Session = Depends(get_session)):
    if current_user.type == 'seller':
        return crud.create_product(db=db, product=product,seller_id=current_user.id)
    else:
        raise HTTPException(status_code=401,detail= "Unauthorized")

@products_router.put("/products/{product_id}")
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_session)):
    updated_product = crud.update_product(db=db, product_id=product_id, product=product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@products_router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_session)):
    deleted_product = crud.delete_product(db=db, product_id=product_id)
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}