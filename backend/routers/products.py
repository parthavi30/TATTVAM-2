from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List, Optional
from schemas.product import ProductResponse, ProductCreate, ProductUpdate, ProductListResponse
from services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=List[ProductResponse])
async def get_products(
    category: Optional[str] = Query(None, description="Filter by category"),
    search: Optional[str] = Query(None, description="Search in name and description"),
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(100, ge=1, le=100, description="Number of items to return")
):
    """Get products with optional filtering and pagination"""
    products = ProductService.get_products(category=category, search=search, skip=skip, limit=limit)
    return products


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int):
    """Get product by ID"""
    product = ProductService.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/categories/list", response_model=List[str])
async def get_categories():
    """Get all product categories"""
    categories = ProductService.get_categories()
    return categories


@router.post("/", response_model=ProductResponse)
async def create_product(product: ProductCreate):
    """Create a new product (admin only)"""
    try:
        new_product = ProductService.create_product(product)
        return new_product
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product: ProductUpdate):
    """Update a product (admin only)"""
    updated_product = ProductService.update_product(product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@router.delete("/{product_id}")
async def delete_product(product_id: int):
    """Delete a product (admin only)"""
    success = ProductService.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}