from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from config import settings
from routers import auth, products, cart, orders
from services.product_service import ProductService

# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    description="Indian E-commerce API for authentic products",
    version=settings.app_version,
    debug=settings.debug
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix=settings.api_v1_prefix)
app.include_router(products.router, prefix=settings.api_v1_prefix)
app.include_router(cart.router, prefix=settings.api_v1_prefix)
app.include_router(orders.router, prefix=settings.api_v1_prefix)

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to Tattvam - Your Indian E-commerce Platform",
        "version": settings.app_version,
        "docs": "/docs",
        "api_prefix": settings.api_v1_prefix
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "tattvam-api"}

# Initialize sample data
@app.on_event("startup")
async def startup_event():
    """Initialize sample data on startup"""
    ProductService.initialize_sample_products()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )