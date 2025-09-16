from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List
from schemas.order import OrderCreate, OrderResponse, OrderListResponse
from services.order_service import OrderService
from routers.auth import get_current_user

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/", response_model=OrderResponse)
async def create_order(
    order: OrderCreate,
    current_user: dict = Depends(get_current_user)
):
    """Create a new order"""
    user_id = current_user["id"]
    try:
        new_order = OrderService.create_order(user_id, order)
        return new_order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[OrderResponse])
async def get_user_orders(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(100, ge=1, le=100, description="Number of items to return"),
    current_user: dict = Depends(get_current_user)
):
    """Get user's orders"""
    user_id = current_user["id"]
    orders = OrderService.get_user_orders(user_id, skip=skip, limit=limit)
    return orders


@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(
    order_id: int,
    current_user: dict = Depends(get_current_user)
):
    """Get order by ID"""
    user_id = current_user["id"]
    order = OrderService.get_order_by_id(order_id)
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Check if order belongs to current user
    if order["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Access denied")
    
    return order


@router.put("/{order_id}/status")
async def update_order_status(
    order_id: int,
    status: str,
    current_user: dict = Depends(get_current_user)
):
    """Update order status (admin only)"""
    user_id = current_user["id"]
    order = OrderService.get_order_by_id(order_id)
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Check if order belongs to current user (for now, allow users to update their own orders)
    if order["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Access denied")
    
    updated_order = OrderService.update_order_status(order_id, status)
    return {"message": "Order status updated successfully", "order": updated_order}