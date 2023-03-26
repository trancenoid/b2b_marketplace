from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    business_category = Column(String)

    products = relationship("Product", back_populates="seller")


class Buyer(Base):
    __tablename__ = "buyers"

    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    business_category = Column(String)

    orders = relationship("Order", back_populates="buyer")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    image = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
    seller_id = Column(Integer, ForeignKey("sellers.id"))

    seller = relationship("Seller", back_populates="products")
    orders = relationship("Order", back_populates="product")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    buyer_id = Column(Integer, ForeignKey("buyers.id"))
    quantity = Column(Integer)
    order_date = Column(String, server_default=func.now())
    comments = Column(String)
    status = Column(String)

    product = relationship("Product", back_populates="orders")
    buyer = relationship("Buyer", back_populates="orders")