from typing import List, Optional
from datetime import datetime
from database import in_memory_storage
from schemas.order import OrderCreate
from services.cart_service import CartService


class OrderService:
    @staticmethod
    def create_order(user_id: int, order_data: OrderCreate) -> dict:
        """Create a new order"""
        # Calculate total amount
        total_amount = sum(
            item["quantity"] * 100.0  # Placeholder price calculation
            for item in order_data.items
        )
        
        # Create order
        order_id = len(in_memory_storage["orders"]) + 1
        order_dict = {
            "id": order_id,
            "user_id": user_id,
            "items": [item.dict() for item in order_data.items],
            "total_amount": total_amount,
            "status": "pending",
            "shipping_address": order_data.shipping_address,
            "created_at": datetime.utcnow().isoformat()
        }
        
        in_memory_storage["orders"][order_id] = order_dict
        
        # Clear user's cart after successful order
        CartService.clear_cart(user_id)
        
        return order_dict
    
    @staticmethod
    def get_user_orders(user_id: int, skip: int = 0, limit: int = 100) -> List[dict]:
        """Get orders for a specific user"""
        user_orders = [
            order for order in in_memory_storage["orders"].values()
            if order["user_id"] == user_id
        ]
        
        # Sort by created_at descending (newest first)
        user_orders.sort(key=lambda x: x["created_at"], reverse=True)
        
        return user_orders[skip:skip + limit]
    
    @staticmethod
    def get_order_by_id(order_id: int) -> Optional[dict]:
        """Get order by ID"""
        return in_memory_storage["orders"].get(order_id)
    
    @staticmethod
    def update_order_status(order_id: int, status: str) -> Optional[dict]:
        """Update order status"""
        if order_id not in in_memory_storage["orders"]:
            return None
        
        order = in_memory_storage["orders"][order_id]
        order["status"] = status
        order["updated_at"] = datetime.utcnow().isoformat()
        
        return order
    
    @staticmethod
    def get_all_orders(skip: int = 0, limit: int = 100) -> List[dict]:
        """Get all orders (admin function)"""
        orders = list(in_memory_storage["orders"].values())
        orders.sort(key=lambda x: x["created_at"], reverse=True)
        return orders[skip:skip + limit]