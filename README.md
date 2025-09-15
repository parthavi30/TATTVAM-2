# Tattvam – Indian E-commerce (React + FastAPI)

Full-stack demo similar to Amazon, focused on Indian products.

- Frontend: React (Vite, TS), TailwindCSS
- Backend: FastAPI (Python), in-memory products/cart
- Dockerized services + docker-compose
- GitHub Actions CI for both apps

## Local development (without Docker)

Frontend:

```bash
cd frontend
npm install
npm run dev
```

Backend:

```bash
cd backend
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Set API URL for frontend (optional):

```bash
# .env.local in frontend
VITE_API_BASE_URL=http://localhost:8000
```

## Run with Docker

```bash
docker compose up --build
```

- Frontend: http://localhost:5173
- Backend: http://localhost:8000

## Project structure

```
backend/
  app/main.py
  requirements.txt
  Dockerfile
frontend/
  src/
  Dockerfile
  nginx.conf
.github/workflows/ci-cd.yml
```

## API endpoints

- GET `/products` – list products
- GET `/products/{id}` – product by id
- GET `/cart` – cart items
- POST `/cart` – add item `{ productId, quantity }`
- PUT `/cart/{productId}` – update quantity `{ quantity }`
- DELETE `/cart/{productId}` – remove item

## CI/CD

GitHub Actions builds both frontend and backend and Docker images on pushes to `main`.

## Notes

- UI uses Tailwind; swap with your preferred component library.
- Data is in-memory for demo purposes; replace with a database when needed.
