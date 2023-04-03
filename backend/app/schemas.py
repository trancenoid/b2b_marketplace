# Defines Pydantic models for the application
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    expires: Optional[datetime] = None


class UserLogin(BaseModel):
    """
    Pydantic model for user login credentials.
    """
    username: str
    password: str

class PasswordReset(BaseModel):
    """
    Pydantic model for password reset request.
    """
    email: str

class UserTypes(Enum):
    BUYER ='buyer'
    SELLER = 'seller'

class UserBase(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str
    type: UserTypes

class User(UserCreate):
    id: int

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    username: str = None
    email: str = None
    password: str = None

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float


class ProductUpdate(BaseModel):
    name: str = None
    description: str = None
    price: float = None

class OrderCreate(BaseModel):
    quantity: int
    total_price: float
    buyer_id: int
    product_id: int


class OrderUpdate(BaseModel):
    quantity: int = None
    total_price: float = None
    buyer_id: int = None
    product_id: int = None


# User schema
class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = False

    class Config:
        orm_mode = True


# Product schema
class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    category_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


# Order schema
class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class Buyer(User):
    orders: List[Order]

    class Config:
        orm_mode = True

class Seller(User):
    products: List[Product]

    class Config:
        orm_mode = True