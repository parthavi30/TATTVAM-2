from typing import List, Optional
from database import in_memory_storage
from schemas.product import ProductCreate, ProductUpdate


class ProductService:
    @staticmethod
    def get_products(
        category: Optional[str] = None, 
        search: Optional[str] = None,
        skip: int = 0,
        limit: int = 100
    ) -> List[dict]:
        """Get products with optional filtering"""
        products = list(in_memory_storage["products"].values())
        
        # Apply filters
        if category:
            products = [p for p in products if p["category"].lower() == category.lower()]
        
        if search:
            search_lower = search.lower()
            products = [p for p in products if 
                       search_lower in p["name"].lower() or 
                       search_lower in p["description"].lower()]
        
        # Apply pagination
        return products[skip:skip + limit]
    
    @staticmethod
    def get_product_by_id(product_id: int) -> Optional[dict]:
        """Get product by ID"""
        return in_memory_storage["products"].get(product_id)
    
    @staticmethod
    def get_categories() -> List[str]:
        """Get all product categories"""
        categories = set()
        for product in in_memory_storage["products"].values():
            categories.add(product["category"])
        return list(categories)
    
    @staticmethod
    def create_product(product_data: ProductCreate) -> dict:
        """Create a new product"""
        product_id = len(in_memory_storage["products"]) + 1
        product_dict = product_data.dict()
        product_dict["id"] = product_id
        product_dict["rating"] = 0.0
        product_dict["reviews_count"] = 0
        product_dict["is_active"] = True
        
        in_memory_storage["products"][product_id] = product_dict
        return product_dict
    
    @staticmethod
    def update_product(product_id: int, product_data: ProductUpdate) -> Optional[dict]:
        """Update an existing product"""
        if product_id not in in_memory_storage["products"]:
            return None
        
        product = in_memory_storage["products"][product_id]
        update_data = product_data.dict(exclude_unset=True)
        
        for field, value in update_data.items():
            product[field] = value
        
        return product
    
    @staticmethod
    def delete_product(product_id: int) -> bool:
        """Delete a product"""
        if product_id in in_memory_storage["products"]:
            del in_memory_storage["products"][product_id]
            return True
        return False
    
    @staticmethod
    def initialize_sample_products():
        """Initialize sample Indian products"""
        sample_products = [
            {
                "name": "Premium Basmati Rice",
                "description": "Aromatic long-grain basmati rice from Punjab",
                "price": 450.0,
                "category": "Food & Grocery",
                "image_url": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400",
                "stock": 100,
                "rating": 4.5,
                "reviews_count": 128
            },
            {
                "name": "Silk Saree - Kanjeevaram",
                "description": "Traditional South Indian silk saree with gold zari work",
                "price": 25000.0,
                "category": "Clothing",
                "image_url": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=400",
                "stock": 15,
                "rating": 4.8,
                "reviews_count": 45
            },
            {
                "name": "Ayurvedic Turmeric Powder",
                "description": "Pure organic turmeric powder for health and beauty",
                "price": 180.0,
                "category": "Health & Wellness",
                "image_url": "https://images.unsplash.com/photo-1609501676725-7186f757a64d?w=400",
                "stock": 200,
                "rating": 4.3,
                "reviews_count": 89
            },
            {
                "name": "Handcrafted Brass Diya Set",
                "description": "Traditional brass oil lamps for festivals and prayers",
                "price": 850.0,
                "category": "Home & Decor",
                "image_url": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400",
                "stock": 50,
                "rating": 4.6,
                "reviews_count": 67
            },
            {
                "name": "Spice Collection - Garam Masala",
                "description": "Authentic blend of Indian spices for traditional cooking",
                "price": 320.0,
                "category": "Food & Grocery",
                "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?w=400",
                "stock": 75,
                "rating": 4.7,
                "reviews_count": 156
            }
        ]
        
        for i, product in enumerate(sample_products, 1):
            product["id"] = i
            product["is_active"] = True
            in_memory_storage["products"][i] = product