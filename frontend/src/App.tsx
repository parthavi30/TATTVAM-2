import { Link, Outlet } from 'react-router-dom'

function App() {
  return (
    <div className="min-h-full bg-white text-gray-900">
      <header className="border-b">
        <div className="mx-auto max-w-7xl px-4 py-4 flex items-center justify-between">
          <Link to="/" className="text-2xl font-bold tracking-tight">
            Tattvam
          </Link>
          <nav className="flex gap-6 text-sm">
            <Link to="/products" className="hover:text-blue-600">Products</Link>
            <Link to="/cart" className="hover:text-blue-600">Cart</Link>
            <Link to="/checkout" className="hover:text-blue-600">Checkout</Link>
          </nav>
        </div>
      </header>
      <main className="mx-auto max-w-7xl px-4 py-8">
        <Outlet />
      </main>
      <footer className="border-t">
        <div className="mx-auto max-w-7xl px-4 py-6 text-sm text-gray-600">
          © {new Date().getFullYear()} Tattvam. All rights reserved.
        </div>
      </footer>
    </div>
  )
}

export default App
