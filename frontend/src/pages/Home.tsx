import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <div className="space-y-8">
      <section className="text-center">
        <h1 className="text-4xl font-semibold">Tattvam</h1>
        <p className="mt-2 text-gray-600">Discover authentic Indian products curated for you.</p>
        <div className="mt-6">
          <Link to="/products" className="inline-block rounded-md bg-blue-600 px-5 py-2 text-white hover:bg-blue-700">
            Shop Now
          </Link>
        </div>
      </section>
      <section>
        <h2 className="text-xl font-semibold mb-4">Popular Categories</h2>
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4">
          {['Handicrafts', 'Spices', 'Textiles', 'Ayurveda'].map((c) => (
            <div key={c} className="rounded-lg border p-4 text-center hover:shadow">
              {c}
            </div>
          ))}
        </div>
      </section>
    </div>
  )
}

