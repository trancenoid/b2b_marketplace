from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class OrderBase(BaseModel):
    product_id: int
    buyer_id: int
    quantity: int
    comments: Optional[str] = None

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    status: Optional[str] = None
    product_id : int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    image: str

class ProductCreate(ProductBase):
    seller_id: int
    quantity: int

class Product(ProductBase):
    id: int
    seller_id: int
    quantity: int
    orders: Optional[List[Order]] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str
    business_name: str
    phone_number: str
    business_category: str

class UserCreate(BaseModel):
    business_name: str
    email: str
    phone_number: str
    business_category: str
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

