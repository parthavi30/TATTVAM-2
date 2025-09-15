import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { getProductById, addToCart, Product as ProductType } from '../services/api'

export default function Product() {
  const { id } = useParams()
  const [product, setProduct] = useState<ProductType | null>(null)
  const [loading, setLoading] = useState<boolean>(true)

  useEffect(() => {
    if (!id) return
    getProductById(id)
      .then(setProduct)
      .finally(() => setLoading(false))
  }, [id])

  if (loading) return <div>Loading...</div>
  if (!product) return <div>Product not found.</div>

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
      <div className="bg-gray-100 rounded aspect-[4/3] flex items-center justify-center overflow-hidden">
        <img src={product.imageUrl} alt={product.name} className="object-cover w-full h-full" />
      </div>
      <div>
        <h1 className="text-2xl font-semibold">{product.name}</h1>
        <p className="mt-2 text-gray-700">{product.description}</p>
        <div className="mt-4 text-xl font-semibold">₹{product.price}</div>
        <button
          className="mt-6 rounded-md bg-blue-600 px-5 py-2 text-white hover:bg-blue-700"
          onClick={() => addToCart(product.id, 1)}
        >
          Add to Cart
        </button>
      </div>
    </div>
  )
}

