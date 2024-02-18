# Contains routes for orders
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_session
from app.database import models
from app.auth import get_current_user
from app.auth.utils import *
from app import schemas


orders_router = APIRouter()


@orders_router.get("/orders/{order_id}", response_model=schemas.Order)
def get_order(order_id: int, current_user : schemas.User = Depends(get_current_user), db: Session = Depends(get_session)):

    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@orders_router.get("/orders/my", response_model=List[schemas.Order])
def get_orders_by_buyer(current_user : schemas.User = Depends(get_current_user),db: Session = Depends(get_session)):
    orders = db.query(models.Order).filter(models.Order.buyer_id == current_user.id).all()
    return orders


@orders_router.get("/orders/seller/{seller_id}", response_model=List[schemas.Order])
def get_orders_by_seller(seller_id: int, db: Session = Depends(get_session)):
    orders = db.query(models.Order).join(models.Product, models.Product.id == models.Order.product_id)\
        .filter(models.Product.seller_id == seller_id).all()
    return orders


@orders_router.post("/orders", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, current_user : schemas.User = Depends(get_current_user),
                  db: Session = Depends(get_session)):
    if current_user.type == "Buyer":
        db_order = models.Order(**order.dict())
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order
    else:
        raise NotAllowedForThisUserTypeException()


@orders_router.put("/orders/{order_id}", response_model=schemas.Order)
def update_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_session)):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    update_data = order.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_order, field, value)
    db.commit()
    db.refresh(db_order)
    return db_order


@orders_router.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_session)):
    db.query(models.Order).filter(models.Order.id == order_id).delete()
    db.commit()
    return {"message": "Order deleted"}