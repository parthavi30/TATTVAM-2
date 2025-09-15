import { useState } from 'react'

export default function Checkout() {
  const [placed, setPlaced] = useState<boolean>(false)

  if (placed) {
    return (
      <div className="space-y-2">
        <h1 className="text-2xl font-semibold">Order Placed</h1>
        <p>Thank you for shopping with Tattvam!</p>
      </div>
    )
  }

  return (
    <div className="max-w-xl">
      <h1 className="text-2xl font-semibold mb-4">Checkout</h1>
      <form
        className="space-y-4"
        onSubmit={(e) => {
          e.preventDefault()
          setPlaced(true)
        }}
      >
        <input className="w-full border rounded p-2" placeholder="Full name" required />
        <input className="w-full border rounded p-2" placeholder="Address" required />
        <input className="w-full border rounded p-2" placeholder="City" required />
        <input className="w-full border rounded p-2" placeholder="Pincode" required />
        <button className="rounded-md bg-blue-600 px-5 py-2 text-white hover:bg-blue-700" type="submit">Place Order</button>
      </form>
    </div>
  )
}

