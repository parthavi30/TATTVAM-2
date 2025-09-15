import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useQuery } from 'react-query';
import { ArrowRight, Star, Truck, Shield, RotateCcw, Headphones } from 'lucide-react';
import { api } from '../services/api';
import ProductCard from '../components/ProductCard';

const Home = () => {
  const [featuredProducts, setFeaturedProducts] = useState([]);

  const { data: categories } = useQuery('categories', () => api.get('/categories').then(res => res.data));

  useEffect(() => {
    // Fetch featured products (top rated)
    api.get('/products')
      .then(res => {
        const products = res.data.sort((a, b) => b.rating - a.rating).slice(0, 8);
        setFeaturedProducts(products);
      })
      .catch(err => console.error('Failed to fetch featured products:', err));
  }, []);

  const features = [
    {
      icon: <Truck className="h-8 w-8 text-primary-500" />,
      title: "Free Delivery",
      description: "Free delivery on orders above ₹500 across India"
    },
    {
      icon: <Shield className="h-8 w-8 text-primary-500" />,
      title: "Secure Payment",
      description: "100% secure payment with SSL encryption"
    },
    {
      icon: <RotateCcw className="h-8 w-8 text-primary-500" />,
      title: "Easy Returns",
      description: "30-day return policy for all products"
    },
    {
      icon: <Headphones className="h-8 w-8 text-primary-500" />,
      title: "24/7 Support",
      description: "Round-the-clock customer support"
    }
  ];

  const categories_data = [
    {
      name: "Food & Grocery",
      image: "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400",
      description: "Authentic Indian spices, rice, and groceries"
    },
    {
      name: "Clothing",
      image: "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=400",
      description: "Traditional Indian clothing and accessories"
    },
    {
      name: "Health & Wellness",
      image: "https://images.unsplash.com/photo-1609501676725-7186f757a64d?w=400",
      description: "Ayurvedic products and wellness items"
    },
    {
      name: "Home & Decor",
      image: "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400",
      description: "Traditional home decor and handicrafts"
    }
  ];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-primary-500 to-saffron-500 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
          <div className="text-center">
            <h1 className="text-4xl md:text-6xl font-bold mb-6">
              Welcome to <span className="text-yellow-300">Tattvam</span>
            </h1>
            <p className="text-xl md:text-2xl mb-8 text-yellow-100">
              Discover Authentic Indian Products
            </p>
            <p className="text-lg mb-10 text-yellow-100 max-w-3xl mx-auto">
              From traditional spices to handcrafted treasures, explore the rich heritage of India 
              with our curated collection of authentic products.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link
                to="/products"
                className="bg-white text-primary-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors flex items-center justify-center"
              >
                Shop Now
                <ArrowRight className="ml-2 h-5 w-5" />
              </Link>
              <Link
                to="/products?category=Food & Grocery"
                className="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-white hover:text-primary-600 transition-colors"
              >
                Explore Categories
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, index) => (
              <div key={index} className="text-center">
                <div className="flex justify-center mb-4">
                  {feature.icon}
                </div>
                <h3 className="text-lg font-semibold text-gray-900 mb-2">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Categories Section */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Shop by Category</h2>
            <p className="text-lg text-gray-600">Explore our diverse range of authentic Indian products</p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {categories_data.map((category, index) => (
              <Link
                key={index}
                to={`/products?category=${encodeURIComponent(category.name)}`}
                className="group bg-white rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300 overflow-hidden"
              >
                <div className="relative">
                  <img
                    src={category.image}
                    alt={category.name}
                    className="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300"
                  />
                  <div className="absolute inset-0 bg-black bg-opacity-20 group-hover:bg-opacity-30 transition-opacity"></div>
                </div>
                <div className="p-6">
                  <h3 className="text-xl font-semibold text-gray-900 mb-2 group-hover:text-primary-600 transition-colors">
                    {category.name}
                  </h3>
                  <p className="text-gray-600">{category.description}</p>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Featured Products Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Featured Products</h2>
            <p className="text-lg text-gray-600">Handpicked products loved by our customers</p>
          </div>
          
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            {featuredProducts.map((product) => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>
          
          <div className="text-center mt-12">
            <Link
              to="/products"
              className="inline-flex items-center bg-primary-500 text-white px-8 py-3 rounded-lg font-semibold hover:bg-primary-600 transition-colors"
            >
              View All Products
              <ArrowRight className="ml-2 h-5 w-5" />
            </Link>
          </div>
        </div>
      </section>

      {/* Newsletter Section */}
      <section className="py-16 bg-primary-500">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl font-bold text-white mb-4">Stay Updated</h2>
          <p className="text-xl text-yellow-100 mb-8">
            Subscribe to our newsletter for the latest offers and new arrivals
          </p>
          <div className="flex flex-col sm:flex-row gap-4 max-w-md mx-auto">
            <input
              type="email"
              placeholder="Enter your email"
              className="flex-1 px-4 py-3 rounded-lg border-0 focus:outline-none focus:ring-2 focus:ring-yellow-300"
            />
            <button className="bg-yellow-400 text-primary-600 px-6 py-3 rounded-lg font-semibold hover:bg-yellow-300 transition-colors">
              Subscribe
            </button>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;