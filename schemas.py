from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Any

class UserBase(BaseModel):
    name: str = Field(...)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(...)

class CategoryBase(BaseModel):
    name: str
    parent_id: Optional[int] = None
    icon: Optional[str] = None
    color: Optional[str] = None

class CategoryOut(CategoryBase):
    id: int
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    image: Optional[str] = None
    price: Optional[float] = None
    previous_price: Optional[float] = None
    supermarket: Optional[str] = None
    category_id: Optional[int] = None

class ProductOut(ProductBase):
    id: int
    class Config:
        orm_mode = True

class FavoriteCreate(BaseModel):
    product_id: int

class ShoppingListCreate(BaseModel):
    name: str
    items: Optional[List[Any]] = []

class AlertCreate(BaseModel):
    product_id: int
    target_price: float
