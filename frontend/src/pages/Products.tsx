import { useEffect, useState } from 'react'
import { getProducts, Product } from '../services/api'
import ProductCard from '../components/ProductCard'

export default function Products() {
  const [products, setProducts] = useState<Product[]>([])
  const [loading, setLoading] = useState<boolean>(true)

  useEffect(() => {
    getProducts()
      .then(setProducts)
      .finally(() => setLoading(false))
  }, [])

  if (loading) {
    return <div>Loading products...</div>
  }

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      {products.map((p) => (
        <ProductCard key={p.id} product={p} />
      ))}
    </div>
  )
}

