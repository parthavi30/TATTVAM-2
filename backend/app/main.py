from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict


app = FastAPI(title="Tattvam API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    imageUrl: str


class CartItem(BaseModel):
    productId: str
    name: str
    price: float
    quantity: int


class AddCartRequest(BaseModel):
    productId: str
    quantity: int


class UpdateCartRequest(BaseModel):
    quantity: int


PRODUCTS: Dict[str, Product] = {
    "1": Product(
        id="1",
        name="Handcrafted Brass Lamp",
        description="Traditional Indian brass lamp.",
        price=1499.0,
        imageUrl="https://picsum.photos/seed/1/800/600",
    ),
    "2": Product(
        id="2",
        name="Organic Turmeric Powder",
        description="High-quality turmeric from Kerala.",
        price=299.0,
        imageUrl="https://picsum.photos/seed/2/800/600",
    ),
    "3": Product(
        id="3",
        name="Khadi Cotton Scarf",
        description="Handwoven scarf in natural dyes.",
        price=799.0,
        imageUrl="https://picsum.photos/seed/3/800/600",
    ),
}

CART: Dict[str, CartItem] = {}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/products", response_model=List[Product])
def list_products():
    return list(PRODUCTS.values())


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str):
    if product_id not in PRODUCTS:
        raise HTTPException(status_code=404, detail="Product not found")
    return PRODUCTS[product_id]


@app.get("/cart", response_model=List[CartItem])
def get_cart():
    return list(CART.values())


@app.post("/cart", response_model=List[CartItem])
def add_to_cart(req: AddCartRequest):
    if req.productId not in PRODUCTS:
        raise HTTPException(status_code=404, detail="Product not found")
    p = PRODUCTS[req.productId]
    if req.productId in CART:
        CART[req.productId].quantity += req.quantity
    else:
        CART[req.productId] = CartItem(
            productId=p.id, name=p.name, price=p.price, quantity=req.quantity
        )
    return list(CART.values())


@app.put("/cart/{product_id}", response_model=List[CartItem])
def update_cart(product_id: str, req: UpdateCartRequest):
    if product_id not in CART:
        raise HTTPException(status_code=404, detail="Item not in cart")
    CART[product_id].quantity = max(1, req.quantity)
    return list(CART.values())


@app.delete("/cart/{product_id}", response_model=List[CartItem])
def remove_cart(product_id: str):
    if product_id in CART:
        del CART[product_id]
    return list(CART.values())

