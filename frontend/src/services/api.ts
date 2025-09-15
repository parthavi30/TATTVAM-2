import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000'

export interface Product {
  id: string
  name: string
  description: string
  price: number
  imageUrl: string
}

export interface CartItem {
  productId: string
  name: string
  price: number
  quantity: number
}

export async function getProducts(): Promise<Product[]> {
  const res = await axios.get(`${API_BASE_URL}/products`)
  return res.data
}

export async function getProductById(id: string): Promise<Product> {
  const res = await axios.get(`${API_BASE_URL}/products/${id}`)
  return res.data
}

export async function addToCart(productId: string, quantity: number): Promise<CartItem[]> {
  const res = await axios.post(`${API_BASE_URL}/cart`, { productId, quantity })
  return res.data
}

export async function getCart(): Promise<CartItem[]> {
  const res = await axios.get(`${API_BASE_URL}/cart`)
  return res.data
}

export async function updateCartItem(productId: string, quantity: number): Promise<CartItem[]> {
  const res = await axios.put(`${API_BASE_URL}/cart/${productId}`, { quantity })
  return res.data
}

export async function removeFromCart(productId: string): Promise<CartItem[]> {
  const res = await axios.delete(`${API_BASE_URL}/cart/${productId}`)
  return res.data
}

