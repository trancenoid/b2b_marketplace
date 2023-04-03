from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    full_name = Column(String)
    type = Column(String)
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }


class Buyer(User):
    __tablename__ = "buyers"

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    orders = relationship("Order", back_populates="buyer")
    __mapper_args__ = {
        "polymorphic_identity": "buyer",
    }


class Seller(User):
    __tablename__ = "sellers"

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    products = relationship("Product", back_populates="seller")
    __mapper_args__ = {
        "polymorphic_identity": "seller",
    }


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    seller_id = Column(Integer, ForeignKey("sellers.id"))

    seller = relationship("Seller", back_populates="products")
    orders = relationship("Order", back_populates="product")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, index=True)
    total_price = Column(Float, index=True)
    buyer_id = Column(Integer, ForeignKey("buyers.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    buyer = relationship("Buyer", back_populates="orders")
    product = relationship("Product", back_populates="orders")