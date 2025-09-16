from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from schemas.cart import CartItemBase


class OrderBase(BaseModel):
    items: List[CartItemBase]
    shipping_address: str


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    status: Optional[str] = None
    shipping_address: Optional[str] = None


class OrderResponse(OrderBase):
    id: int
    user_id: int
    total_amount: float
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class OrderListResponse(BaseModel):
    orders: List[OrderResponse]
    total: int
    page: int
    size: int