# Contains CRUD operations for the database
from typing import List, Optional
from sqlalchemy.orm import Session
from . import models
from app.schemas import *

def get_user(db: Session, user_id: int) -> Optional[models.User]:
    """
    Retrieve a user by their ID.
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    """
    Retrieve a user by their email address.
    """
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_username(db: Session, username: str) -> Optional[models.User]:
    """
    Retrieve a user by their username.
    """
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    """
    Retrieve all users.
    """
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate) -> models.User:
    """
    Create a new user.
    """
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: UserUpdate) -> Optional[models.User]:
    """
    Update an existing user.
    """
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int) -> Optional[models.User]:
    """
    Delete a user.
    """
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


def get_product(db: Session, product_id: int) -> Optional[models.Product]:
    """
    Retrieve a product by its ID.
    """
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 100) -> List[models.Product]:
    """
    Retrieve all products.
    """
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: ProductCreate, seller_id: int) -> models.Product:
    """
    Create a new product.
    """
    db_product = models.Product(**product.dict(), seller_id=seller_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, product: ProductUpdate) -> Optional[models.Product]:
    """
    Update an existing product.
    """
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        for var, value in vars(product).items():
            setattr(db_product, var, value) if value else None
        db.commit()
        db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int) -> Optional[models.Product]:
    """
    Delete a product.
    """
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
       

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def get_orders_by_buyer(db: Session, buyer_id: int):
    return db.query(models.Order).filter(models.Order.buyer_id == buyer_id).all()


def get_orders_by_seller(db: Session, seller_id: int):
    return db.query(models.Order).join(models.Product, models.Product.id == models.Order.product_id)\
        .filter(models.Product.seller_id == seller_id).all()


def create_order(db: Session, order: OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def update_order(db: Session, order_id: int, order: OrderUpdate):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    for field, value in order:
        setattr(db_order, field, value)
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_order(db: Session, order_id: int):
    db.query(models.Order).filter(models.Order.id == order_id).delete()
    db.commit()
    return {"message": "Order deleted"}