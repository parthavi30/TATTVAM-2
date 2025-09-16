from pydantic import BaseModel
from typing import List
from schemas.product import ProductResponse


class CartItemBase(BaseModel):
    product_id: int
    quantity: int


class CartItemCreate(CartItemBase):
    pass


class CartItemResponse(CartItemBase):
    product: ProductResponse

    class Config:
        from_attributes = True


class CartResponse(BaseModel):
    items: List[CartItemResponse]
    total_items: int
    total_amount: float