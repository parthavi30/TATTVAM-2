# Tattvam - Indian E-commerce Platform

![Tattvam Logo](https://img.shields.io/badge/Tattvam-Indian%20E--commerce-orange?style=for-the-badge&logo=shopping-cart)

A modern, full-stack e-commerce platform specializing in authentic Indian products. Built with React.js, FastAPI, and Docker for a seamless shopping experience.

## 🌟 Features

- **Authentic Indian Products**: Curated collection of traditional Indian items
- **Modern UI/UX**: Beautiful, responsive design with Tailwind CSS
- **User Authentication**: Secure login/registration system
- **Shopping Cart**: Add, remove, and manage items
- **Order Management**: Track orders and view order history
- **Product Categories**: Food & Grocery, Clothing, Health & Wellness, Home & Decor
- **Search & Filter**: Find products easily with advanced search
- **Mobile Responsive**: Works perfectly on all devices
- **Dockerized**: Easy deployment with Docker containers
- **CI/CD Pipeline**: Automated testing and deployment

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React Frontend│    │   FastAPI       │    │   Database      │
│   (Port 3000)   │◄──►│   Backend       │◄──►│   (Future)      │
│                 │    │   (Port 8000)   │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.11+ (for local development)

### Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/tattvam.git
   cd tattvam
   ```

2. **Start the application**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Local Development

#### Backend Setup

1. **Navigate to backend directory**
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

#### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```

## 📁 Project Structure

```
tattvam/
├── backend/                 # FastAPI backend
│   ├── main.py             # Main application file
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile         # Backend Docker configuration
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # Reusable components
│   │   ├── pages/         # Page components
│   │   ├── contexts/      # React contexts
│   │   ├── services/      # API services
│   │   └── App.js         # Main App component
│   ├── package.json       # Node.js dependencies
│   ├── tailwind.config.js # Tailwind CSS configuration
│   └── Dockerfile         # Frontend Docker configuration
├── .github/
│   └── workflows/         # GitHub Actions CI/CD
├── docker-compose.yml     # Docker Compose configuration
└── README.md             # This file
```

## 🛠️ Technology Stack

### Frontend
- **React 18**: Modern React with hooks
- **React Router**: Client-side routing
- **Tailwind CSS**: Utility-first CSS framework
- **Lucide React**: Beautiful icons
- **React Query**: Data fetching and caching
- **React Hot Toast**: Notifications
- **Axios**: HTTP client

### Backend
- **FastAPI**: Modern, fast web framework
- **Python 3.11**: Programming language
- **JWT**: Authentication tokens
- **Pydantic**: Data validation
- **Uvicorn**: ASGI server

### DevOps
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration
- **GitHub Actions**: CI/CD pipeline
- **Nginx**: Web server for production

## 🔧 API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login

### Products
- `GET /products` - Get all products
- `GET /products/{id}` - Get product by ID
- `GET /categories` - Get product categories

### Cart
- `GET /cart` - Get user's cart
- `POST /cart/add` - Add item to cart
- `DELETE /cart/{product_id}` - Remove item from cart

### Orders
- `GET /orders` - Get user's orders
- `POST /orders` - Create new order

### Profile
- `GET /profile` - Get user profile

## 🎨 UI Components

- **Navbar**: Navigation with search and cart
- **ProductCard**: Product display component
- **Cart**: Shopping cart management
- **ProductDetail**: Detailed product view
- **Login/Register**: Authentication forms
- **Profile**: User profile management
- **Orders**: Order history and tracking

## 🚀 Deployment

### Production Deployment

1. **Build production images**
   ```bash
   docker-compose -f docker-compose.prod.yml up --build
   ```

2. **Environment Variables**
   ```bash
   # Backend
   SECRET_KEY=your-secret-key
   
   # Frontend
   REACT_APP_API_URL=https://your-api-domain.com
   ```

### Cloud Deployment

The application is ready for deployment on:
- **AWS**: Using ECS, EKS, or EC2
- **Google Cloud**: Using Cloud Run or GKE
- **Azure**: Using Container Instances or AKS
- **DigitalOcean**: Using App Platform or Droplets

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest --cov=. --cov-report=html
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 📊 CI/CD Pipeline

The GitHub Actions workflow includes:
- **Testing**: Automated tests for both frontend and backend
- **Security Scanning**: Vulnerability scanning with Trivy
- **Building**: Docker image building and pushing
- **Deployment**: Automated deployment to production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

- **Full Stack Developer**: Senior developer with expertise in React and FastAPI
- **UI/UX Designer**: Focus on Indian cultural aesthetics
- **DevOps Engineer**: Docker and CI/CD pipeline management

## 🆘 Support

For support, email support@tattvam.com or join our Slack channel.

## 🔮 Future Enhancements

- [ ] Payment gateway integration (Razorpay, PayU)
- [ ] Real-time notifications
- [ ] Advanced search with filters
- [ ] Product reviews and ratings
- [ ] Wishlist functionality
- [ ] Multi-language support
- [ ] Mobile app (React Native)
- [ ] Admin dashboard
- [ ] Inventory management
- [ ] Analytics and reporting

---

**Made with ❤️ for authentic Indian products**