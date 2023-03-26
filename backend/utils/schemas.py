from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# will OrderUpdate be same as OrderCreate ? 

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
    order_status: Optional[str] = None

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str
    business_name: str
    phone_number: str
    business_category: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    image_url: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    seller_id: int

    class Config:
        orm_mode = True