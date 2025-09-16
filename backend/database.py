# Database configuration and connection setup
# This file will be used when we integrate with a real database (PostgreSQL, etc.)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

# For now, we'll use in-memory storage
# In the future, this will be replaced with actual database connection

# Database URL (will be used when we add PostgreSQL)
# SQLALCHEMY_DATABASE_URL = settings.database_url or "sqlite:///./tattvam.db"

# For future database integration:
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# For now, we'll use in-memory storage
# This will be replaced with actual database operations
in_memory_storage = {
    "users": {},
    "products": {},
    "orders": {},
    "cart": {}
}