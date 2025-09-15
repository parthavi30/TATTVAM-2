import { Link } from 'react-router-dom'
import { Product } from '../services/api'

interface ProductCardProps {
  product: Product
}

export default function ProductCard({ product }: ProductCardProps) {
  return (
    <div className="rounded-lg border p-4 flex flex-col">
      <div className="aspect-[4/3] bg-gray-100 rounded mb-3 overflow-hidden flex items-center justify-center">
        <img src={product.imageUrl} alt={product.name} className="object-cover w-full h-full" />
      </div>
      <div className="flex-1">
        <h3 className="font-medium">{product.name}</h3>
        <p className="text-sm text-gray-600 line-clamp-2">{product.description}</p>
      </div>
      <div className="mt-3 flex items-center justify-between">
        <span className="font-semibold">₹{product.price}</span>
        <Link to={`/products/${product.id}`} className="text-blue-600 hover:underline">View</Link>
      </div>
    </div>
  )
}

