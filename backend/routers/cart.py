from fastapi import APIRouter, HTTPException, Depends
from schemas.cart import CartItemCreate, CartResponse
from services.cart_service import CartService
from routers.auth import get_current_user

router = APIRouter(prefix="/cart", tags=["cart"])


@router.get("/", response_model=CartResponse)
async def get_cart(current_user: dict = Depends(get_current_user)):
    """Get user's cart"""
    user_id = current_user["id"]
    cart_items = CartService.get_cart(user_id)
    total_amount = CartService.get_cart_total(user_id)
    total_items = CartService.get_cart_items_count(user_id)
    
    return {
        "items": cart_items,
        "total_items": total_items,
        "total_amount": total_amount
    }


@router.post("/add")
async def add_to_cart(
    cart_item: CartItemCreate,
    current_user: dict = Depends(get_current_user)
):
    """Add item to cart"""
    user_id = current_user["id"]
    try:
        result = CartService.add_to_cart(user_id, cart_item)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{product_id}")
async def remove_from_cart(
    product_id: int,
    current_user: dict = Depends(get_current_user)
):
    """Remove item from cart"""
    user_id = current_user["id"]
    success = CartService.remove_from_cart(user_id, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found in cart")
    return {"message": "Item removed from cart"}


@router.put("/{product_id}")
async def update_cart_item_quantity(
    product_id: int,
    quantity: int,
    current_user: dict = Depends(get_current_user)
):
    """Update item quantity in cart"""
    user_id = current_user["id"]
    success = CartService.update_cart_item_quantity(user_id, product_id, quantity)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found in cart")
    return {"message": "Cart updated successfully"}


@router.delete("/")
async def clear_cart(current_user: dict = Depends(get_current_user)):
    """Clear user's cart"""
    user_id = current_user["id"]
    success = CartService.clear_cart(user_id)
    return {"message": "Cart cleared successfully"}