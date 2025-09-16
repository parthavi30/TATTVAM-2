import hashlib
import jwt
from datetime import datetime, timedelta
from typing import Optional
from config import settings
from database import in_memory_storage
from schemas.user import UserCreate, UserLogin, TokenData


class AuthService:
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify password against hash"""
        return AuthService.hash_password(plain_password) == hashed_password
    
    @staticmethod
    def create_access_token(data: dict) -> str:
        """Create JWT access token"""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
        return encoded_jwt
    
    @staticmethod
    def verify_token(token: str) -> Optional[TokenData]:
        """Verify JWT token and return token data"""
        try:
            payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
            user_id = payload.get("sub")
            if user_id is None:
                return None
            return TokenData(user_id=int(user_id))
        except jwt.PyJWTError:
            return None
    
    @staticmethod
    def register_user(user_data: UserCreate) -> dict:
        """Register a new user"""
        # Check if email already exists
        for user in in_memory_storage["users"].values():
            if user["email"] == user_data.email:
                raise ValueError("Email already registered")
        
        # Check if username already exists
        for user in in_memory_storage["users"].values():
            if user["username"] == user_data.username:
                raise ValueError("Username already taken")
        
        # Create new user
        user_id = len(in_memory_storage["users"]) + 1
        user_dict = user_data.dict()
        user_dict["id"] = user_id
        user_dict["password"] = AuthService.hash_password(user_data.password)
        user_dict["is_active"] = True
        user_dict["created_at"] = datetime.utcnow().isoformat()
        
        in_memory_storage["users"][user_id] = user_dict
        
        # Remove password from response
        user_dict.pop("password", None)
        return user_dict
    
    @staticmethod
    def authenticate_user(login_data: UserLogin) -> Optional[dict]:
        """Authenticate user and return user data if valid"""
        for user in in_memory_storage["users"].values():
            if (user["email"] == login_data.email and 
                AuthService.verify_password(login_data.password, user["password"])):
                # Remove password from response
                user_dict = user.copy()
                user_dict.pop("password", None)
                return user_dict
        return None