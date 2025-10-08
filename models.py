from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON
from db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), unique=True, index=True, nullable=False)
    hashed_password = Column(String(512), nullable=False)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    icon = Column(String(200), nullable=True)
    color = Column(String(50), nullable=True)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(300), nullable=False)
    image = Column(String(1000), nullable=True)
    price = Column(Float, nullable=True)
    previous_price = Column(Float, nullable=True)
    supermarket = Column(String(200), nullable=True)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True)

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))

class ShoppingList(Base):
    __tablename__ = 'shopping_lists'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(300), nullable=False)
    items = Column(JSON, nullable=True)

class Alert(Base):
    __tablename__ = 'alerts'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    target_price = Column(Float, nullable=False)
