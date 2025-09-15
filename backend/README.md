# Tattvam Backend API

FastAPI-based backend for the Tattvam e-commerce platform, providing RESTful APIs for Indian product management.

## 🚀 Features

- **FastAPI Framework**: High-performance async API
- **JWT Authentication**: Secure user authentication
- **Product Management**: CRUD operations for products
- **Cart Management**: Shopping cart functionality
- **Order Processing**: Order creation and management
- **User Profiles**: User account management
- **CORS Support**: Cross-origin resource sharing
- **Auto Documentation**: Interactive API docs with Swagger

## 📋 API Endpoints

### Authentication
```
POST /auth/register     - Register new user
POST /auth/login        - User login
```

### Products
```
GET  /products          - Get all products (with filters)
GET  /products/{id}     - Get product by ID
GET  /categories        - Get product categories
```

### Cart Management
```
GET    /cart            - Get user's cart
POST   /cart/add        - Add item to cart
DELETE /cart/{id}       - Remove item from cart
```

### Orders
```
GET  /orders            - Get user's orders
POST /orders            - Create new order
```

### User Profile
```
GET  /profile           - Get user profile
PUT  /profile           - Update user profile
```

## 🛠️ Setup

### Prerequisites
- Python 3.11+
- pip

### Installation

1. **Clone and navigate to backend**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Using Docker

```bash
docker build -t tattvam-backend .
docker run -p 8000:8000 tattvam-backend
```

## 📊 Data Models

### User
```python
{
    "id": int,
    "username": str,
    "email": str,
    "password": str,  # hashed
    "full_name": str,
    "address": str,
    "phone": str
}
```

### Product
```python
{
    "id": int,
    "name": str,
    "description": str,
    "price": float,
    "category": str,
    "image_url": str,
    "stock": int,
    "rating": float,
    "reviews_count": int
}
```

### Order
```python
{
    "id": int,
    "user_id": int,
    "items": List[CartItem],
    "total_amount": float,
    "status": str,
    "shipping_address": str,
    "created_at": datetime
}
```

## 🔐 Authentication

The API uses JWT tokens for authentication:

1. **Register/Login** to get an access token
2. **Include token** in Authorization header: `Bearer <token>`
3. **Token expires** after 24 hours

### Example Usage
```python
import requests

# Login
response = requests.post("http://localhost:8000/auth/login", json={
    "email": "user@example.com",
    "password": "password123"
})
token = response.json()["access_token"]

# Use token for authenticated requests
headers = {"Authorization": f"Bearer {token}"}
response = requests.get("http://localhost:8000/profile", headers=headers)
```

## 🧪 Testing

### Run Tests
```bash
pytest --cov=. --cov-report=html
```

### Test Coverage
- Unit tests for all endpoints
- Authentication tests
- Data validation tests
- Error handling tests

## 📚 API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔧 Configuration

### Environment Variables
```bash
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:pass@localhost/db  # Future use
```

### CORS Settings
The API is configured to accept requests from:
- `http://localhost:3000` (React dev server)
- `http://frontend:3000` (Docker container)

## 🚀 Production Deployment

### Using Docker
```bash
docker build -t tattvam-backend .
docker run -d -p 8000:8000 --name tattvam-backend tattvam-backend
```

### Environment Setup
```bash
export SECRET_KEY="your-production-secret-key"
export DATABASE_URL="your-production-database-url"
```

## 📈 Performance

- **Async/Await**: Non-blocking I/O operations
- **Pydantic**: Fast data validation
- **Uvicorn**: High-performance ASGI server
- **Connection Pooling**: Efficient database connections (future)

## 🔒 Security Features

- **JWT Tokens**: Secure authentication
- **Password Hashing**: SHA-256 password hashing
- **CORS Protection**: Cross-origin request validation
- **Input Validation**: Pydantic model validation
- **Error Handling**: Secure error responses

## 🐛 Error Handling

The API returns structured error responses:

```json
{
    "detail": "Error message",
    "status_code": 400
}
```

Common HTTP status codes:
- `200`: Success
- `201`: Created
- `400`: Bad Request
- `401`: Unauthorized
- `404`: Not Found
- `422`: Validation Error
- `500`: Internal Server Error

## 🔮 Future Enhancements

- [ ] Database integration (PostgreSQL)
- [ ] Redis caching
- [ ] Rate limiting
- [ ] Email notifications
- [ ] File upload for product images
- [ ] Advanced search with Elasticsearch
- [ ] Payment gateway integration
- [ ] Admin panel APIs
- [ ] Analytics endpoints
- [ ] WebSocket for real-time updates

## 📞 Support

For API support or questions:
- Create an issue in the repository
- Email: api-support@tattvam.com
- Documentation: http://localhost:8000/docs