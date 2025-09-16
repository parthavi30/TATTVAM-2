from typing import List, Optional
from database import in_memory_storage
from schemas.cart import CartItemCreate
from services.product_service import ProductService


class CartService:
    @staticmethod
    def get_cart(user_id: int) -> List[dict]:
        """Get user's cart items"""
        if user_id not in in_memory_storage["cart"]:
            return []
        
        cart_items = []
        for item in in_memory_storage["cart"][user_id]:
            product = ProductService.get_product_by_id(item["product_id"])
            if product:
                cart_items.append({
                    "product": product,
                    "quantity": item["quantity"]
                })
        
        return cart_items
    
    @staticmethod
    def add_to_cart(user_id: int, cart_item: CartItemCreate) -> dict:
        """Add item to user's cart"""
        # Verify product exists
        product = ProductService.get_product_by_id(cart_item.product_id)
        if not product:
            raise ValueError("Product not found")
        
        # Initialize cart if it doesn't exist
        if user_id not in in_memory_storage["cart"]:
            in_memory_storage["cart"][user_id] = []
        
        # Check if item already in cart
        for item in in_memory_storage["cart"][user_id]:
            if item["product_id"] == cart_item.product_id:
                item["quantity"] += cart_item.quantity
                return {"message": "Item quantity updated in cart"}
        
        # Add new item to cart
        in_memory_storage["cart"][user_id].append(cart_item.dict())
        return {"message": "Item added to cart"}
    
    @staticmethod
    def remove_from_cart(user_id: int, product_id: int) -> bool:
        """Remove item from user's cart"""
        if user_id not in in_memory_storage["cart"]:
            return False
        
        cart = in_memory_storage["cart"][user_id]
        original_length = len(cart)
        in_memory_storage["cart"][user_id] = [
            item for item in cart if item["product_id"] != product_id
        ]
        
        return len(in_memory_storage["cart"][user_id]) < original_length
    
    @staticmethod
    def update_cart_item_quantity(user_id: int, product_id: int, quantity: int) -> bool:
        """Update quantity of item in cart"""
        if user_id not in in_memory_storage["cart"]:
            return False
        
        for item in in_memory_storage["cart"][user_id]:
            if item["product_id"] == product_id:
                if quantity <= 0:
                    return CartService.remove_from_cart(user_id, product_id)
                else:
                    item["quantity"] = quantity
                    return True
        
        return False
    
    @staticmethod
    def clear_cart(user_id: int) -> bool:
        """Clear user's cart"""
        if user_id in in_memory_storage["cart"]:
            in_memory_storage["cart"][user_id] = []
            return True
        return False
    
    @staticmethod
    def get_cart_total(user_id: int) -> float:
        """Calculate total amount of items in cart"""
        cart_items = CartService.get_cart(user_id)
        total = 0.0
        
        for item in cart_items:
            total += item["product"]["price"] * item["quantity"]
        
        return total
    
    @staticmethod
    def get_cart_items_count(user_id: int) -> int:
        """Get total number of items in cart"""
        cart_items = CartService.get_cart(user_id)
        return sum(item["quantity"] for item in cart_items)