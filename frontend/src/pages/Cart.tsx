import { useEffect, useState } from 'react'
import { getCart, removeFromCart, updateCartItem, CartItem } from '../services/api'
import { Link } from 'react-router-dom'

export default function Cart() {
  const [items, setItems] = useState<CartItem[]>([])

  useEffect(() => {
    getCart().then(setItems)
  }, [])

  const total = items.reduce((sum, i) => sum + i.price * i.quantity, 0)

  return (
    <div>
      <h1 className="text-2xl font-semibold mb-4">Your Cart</h1>
      {items.length === 0 ? (
        <div>
          <p>Your cart is empty.</p>
          <Link className="text-blue-600 hover:underline" to="/products">Continue shopping</Link>
        </div>
      ) : (
        <div className="space-y-4">
          {items.map((item) => (
            <div key={item.productId} className="flex items-center justify-between border rounded p-3">
              <div>
                <div className="font-medium">{item.name}</div>
                <div className="text-sm text-gray-600">₹{item.price}</div>
              </div>
              <div className="flex items-center gap-2">
                <button className="px-2 border rounded" onClick={() => updateCartItem(item.productId, Math.max(1, item.quantity - 1)).then(setItems)}>-</button>
                <span>{item.quantity}</span>
                <button className="px-2 border rounded" onClick={() => updateCartItem(item.productId, item.quantity + 1).then(setItems)}>+</button>
                <button className="ml-2 text-red-600" onClick={() => removeFromCart(item.productId).then(setItems)}>Remove</button>
              </div>
            </div>
          ))}
          <div className="flex items-center justify-between mt-6">
            <div className="text-lg font-semibold">Total: ₹{total}</div>
            <Link className="rounded-md bg-blue-600 px-5 py-2 text-white hover:bg-blue-700" to="/checkout">Checkout</Link>
          </div>
        </div>
      )}
    </div>
  )
}

