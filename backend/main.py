from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import jwt
from datetime import datetime, timedelta
import hashlib
import os

app = FastAPI(title="Tattvam API", description="Indian E-commerce API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://frontend:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer()
SECRET_KEY = os.getenv("SECRET_KEY", "tattvam-secret-key-2024")
ALGORITHM = "HS256"

# Database models (in-memory for demo)
users_db = {}
products_db = {}
orders_db = {}
cart_db = {}

# Pydantic models
class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    full_name: str
    address: Optional[str] = None
    phone: Optional[str] = None

class UserLogin(BaseModel):
    email: str
    password: str

class Product(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    price: float
    category: str
    image_url: str
    stock: int
    rating: float = 0.0
    reviews_count: int = 0

class CartItem(BaseModel):
    product_id: int
    quantity: int

class Order(BaseModel):
    id: Optional[int] = None
    user_id: int
    items: List[CartItem]
    total_amount: float
    status: str = "pending"
    shipping_address: str
    created_at: Optional[datetime] = None

# Authentication functions
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return int(user_id)
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Initialize sample data
def init_sample_data():
    sample_products = [
        {
            "id": 1,
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
            "id": 2,
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
            "id": 3,
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
            "id": 4,
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
            "id": 5,
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
    
    for product in sample_products:
        products_db[product["id"]] = product

# Routes
@app.get("/")
async def root():
    return {"message": "Welcome to Tattvam - Your Indian E-commerce Platform"}

@app.post("/auth/register")
async def register(user: User):
    if user.email in [u["email"] for u in users_db.values()]:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_id = len(users_db) + 1
    user_data = user.dict()
    user_data["id"] = user_id
    user_data["password"] = hash_password(user.password)
    users_db[user_id] = user_data
    
    access_token = create_access_token(data={"sub": str(user_id)})
    return {"access_token": access_token, "token_type": "bearer", "user": user_data}

@app.post("/auth/login")
async def login(user_login: UserLogin):
    for user in users_db.values():
        if user["email"] == user_login.email and user["password"] == hash_password(user_login.password):
            access_token = create_access_token(data={"sub": str(user["id"])})
            return {"access_token": access_token, "token_type": "bearer", "user": user}
    
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/products")
async def get_products(category: Optional[str] = None, search: Optional[str] = None):
    products = list(products_db.values())
    
    if category:
        products = [p for p in products if p["category"].lower() == category.lower()]
    
    if search:
        products = [p for p in products if search.lower() in p["name"].lower() or search.lower() in p["description"].lower()]
    
    return products

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]

@app.get("/categories")
async def get_categories():
    categories = list(set(product["category"] for product in products_db.values()))
    return categories

@app.post("/cart/add")
async def add_to_cart(cart_item: CartItem, user_id: int = Depends(verify_token)):
    if cart_item.product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if user_id not in cart_db:
        cart_db[user_id] = []
    
    # Check if item already in cart
    for item in cart_db[user_id]:
        if item["product_id"] == cart_item.product_id:
            item["quantity"] += cart_item.quantity
            return {"message": "Item quantity updated in cart"}
    
    cart_db[user_id].append(cart_item.dict())
    return {"message": "Item added to cart"}

@app.get("/cart")
async def get_cart(user_id: int = Depends(verify_token)):
    if user_id not in cart_db:
        return []
    
    cart_items = []
    for item in cart_db[user_id]:
        product = products_db[item["product_id"]]
        cart_items.append({
            "product": product,
            "quantity": item["quantity"]
        })
    
    return cart_items

@app.delete("/cart/{product_id}")
async def remove_from_cart(product_id: int, user_id: int = Depends(verify_token)):
    if user_id not in cart_db:
        raise HTTPException(status_code=404, detail="Cart not found")
    
    cart_db[user_id] = [item for item in cart_db[user_id] if item["product_id"] != product_id]
    return {"message": "Item removed from cart"}

@app.post("/orders")
async def create_order(order: Order, user_id: int = Depends(verify_token)):
    order_id = len(orders_db) + 1
    order_data = order.dict()
    order_data["id"] = order_id
    order_data["user_id"] = user_id
    order_data["created_at"] = datetime.utcnow()
    orders_db[order_id] = order_data
    
    # Clear cart after order
    if user_id in cart_db:
        cart_db[user_id] = []
    
    return {"order_id": order_id, "message": "Order created successfully"}

@app.get("/orders")
async def get_orders(user_id: int = Depends(verify_token)):
    user_orders = [order for order in orders_db.values() if order["user_id"] == user_id]
    return user_orders

@app.get("/profile")
async def get_profile(user_id: int = Depends(verify_token)):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

if __name__ == "__main__":
    init_sample_data()
    uvicorn.run(app, host="0.0.0.0", port=8000)