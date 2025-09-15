#!/bin/bash

# Tattvam Deployment Script
# This script helps deploy the Tattvam e-commerce platform

set -e

echo "🚀 Starting Tattvam deployment..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Docker is installed
check_docker() {
    print_status "Checking Docker installation..."
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed. Please install Docker first."
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose is not installed. Please install Docker Compose first."
        exit 1
    fi
    
    print_success "Docker and Docker Compose are installed"
}

# Check if environment files exist
check_env_files() {
    print_status "Checking environment files..."
    
    if [ ! -f "backend/.env" ]; then
        print_warning "backend/.env not found. Creating from example..."
        cp backend/.env.example backend/.env
        print_warning "Please update backend/.env with your configuration"
    fi
    
    if [ ! -f "frontend/.env" ]; then
        print_warning "frontend/.env not found. Creating from example..."
        cp frontend/.env.example frontend/.env
        print_warning "Please update frontend/.env with your configuration"
    fi
    
    print_success "Environment files checked"
}

# Build and start services
deploy_services() {
    print_status "Building and starting services..."
    
    # Stop existing containers
    print_status "Stopping existing containers..."
    docker-compose down 2>/dev/null || true
    
    # Build and start services
    print_status "Building Docker images..."
    docker-compose build --no-cache
    
    print_status "Starting services..."
    docker-compose up -d
    
    print_success "Services started successfully"
}

# Check service health
check_health() {
    print_status "Checking service health..."
    
    # Wait for services to start
    sleep 10
    
    # Check backend
    if curl -f http://localhost:8000/ > /dev/null 2>&1; then
        print_success "Backend is healthy"
    else
        print_error "Backend health check failed"
        return 1
    fi
    
    # Check frontend
    if curl -f http://localhost:3000/ > /dev/null 2>&1; then
        print_success "Frontend is healthy"
    else
        print_error "Frontend health check failed"
        return 1
    fi
}

# Show deployment information
show_info() {
    print_success "🎉 Tattvam deployment completed successfully!"
    echo ""
    echo "📱 Application URLs:"
    echo "   Frontend: http://localhost:3000"
    echo "   Backend API: http://localhost:8000"
    echo "   API Documentation: http://localhost:8000/docs"
    echo ""
    echo "🔧 Management Commands:"
    echo "   View logs: docker-compose logs -f"
    echo "   Stop services: docker-compose down"
    echo "   Restart services: docker-compose restart"
    echo "   Update services: docker-compose pull && docker-compose up -d"
    echo ""
    echo "📊 Sample Products Available:"
    echo "   - Premium Basmati Rice"
    echo "   - Silk Saree - Kanjeevaram"
    echo "   - Ayurvedic Turmeric Powder"
    echo "   - Handcrafted Brass Diya Set"
    echo "   - Spice Collection - Garam Masala"
    echo ""
    print_status "Happy shopping! 🛒"
}

# Main deployment function
main() {
    echo "🏪 Tattvam - Indian E-commerce Platform"
    echo "======================================"
    echo ""
    
    check_docker
    check_env_files
    deploy_services
    
    if check_health; then
        show_info
    else
        print_error "Deployment completed but health checks failed"
        print_status "Check logs with: docker-compose logs"
        exit 1
    fi
}

# Handle script arguments
case "${1:-}" in
    "stop")
        print_status "Stopping Tattvam services..."
        docker-compose down
        print_success "Services stopped"
        ;;
    "restart")
        print_status "Restarting Tattvam services..."
        docker-compose restart
        print_success "Services restarted"
        ;;
    "logs")
        docker-compose logs -f
        ;;
    "update")
        print_status "Updating Tattvam services..."
        docker-compose pull
        docker-compose up -d
        print_success "Services updated"
        ;;
    "help"|"-h"|"--help")
        echo "Tattvam Deployment Script"
        echo ""
        echo "Usage: $0 [command]"
        echo ""
        echo "Commands:"
        echo "  (no args)  Deploy the application"
        echo "  stop       Stop all services"
        echo "  restart    Restart all services"
        echo "  logs       Show service logs"
        echo "  update     Update and restart services"
        echo "  help       Show this help message"
        ;;
    *)
        main
        ;;
esac