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
    username: str
    business_name: str
    phone_number: str
    business_category: str
    usertype: str

class UserCreate(UserBase):
    password: str
    
class UserLogin(BaseModel):
    username: str
    password: str
    usertype: str
