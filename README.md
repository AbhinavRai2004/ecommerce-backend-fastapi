# 🚀E-Commerce API 🛒

Welcome to the backend engine for a modern e-commerce platform, crafted with precision using **FastAPI** and the asynchronous power of **MongoDB**. This project delivers a high-performance, scalable API for managing products and orders, built as a submission for the **HROne Backend Intern Hiring Task**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/FastAPI-0.100+-05998b?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB Atlas">
  <img src="https://img.shields.io/badge/Deployment-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" alt="Render Deployment">
</p>

---

## ✨ Core Features

This API isn't just a basic backend; it's a showcase of modern development practices and robust functionality.

* ⚡ Async Everywhere: Leverages Python's `async/await` with the `motor` driver for non-blocking database operations, ensuring maximum throughput.
* 📦 Dynamic Product Catalog: Easily create products and list them with powerful, chainable filters for name and size.
* 🗂️ Built-in Pagination: All list endpoints (`GET /products`, `GET /orders/{userId}`) come with `limit` and `offset` query parameters for smooth, predictable pagination.
* 🏗️ Modular Architecture: Organized with FastAPI's `APIRouter` for clean separation of concerns, making the codebase easy to navigate and extend.
* ☁️ Cloud Native: Seamlessly deployed to **Render** and connected to a **MongoDB Atlas** cluster, ready for the web.

---

## 🏛️ Project Architecture

The project is structured logically to separate database logic, API routing, and data schemas.

```
hrone_fastapi_backend/
├── app/
│   ├── db.py               # Configures the async MongoDB client (Motor)
│   ├── main.py             # FastAPI application entry point and middleware
│   ├── models/             # Helper functions to format data for MongoDB
│   ├── routes/             # API endpoint definitions (APIRouter)
│   └── schemas/            # Pydantic models for data validation & serialization
├── .env                    # Environment variables (ignored by git)
└── requirements.txt        # Project dependencies
```

---

## 🧰 Tech Stack

| Component    | Technology                                                              | Reason                                                 |
|--------------|-------------------------------------------------------------------------|--------------------------------------------------------|
| **Language** | Python 3.11+                                                             | Modern syntax, type hints, and performance improvements. |
| **Framework**| FastAPI                                                                  | High-speed, async-native, with automatic API docs.     |
| **Database** | MongoDB (via Atlas M0 Cluster)                                           | Flexible, scalable NoSQL database for document data.   |
| **Driver**   | Motor                                                                    | The official async driver for MongoDB in Python.       |
| **Deployment**| Render (Free Plan)                                                      | Git-push-to-deploy platform with free SSL and CI/CD.   |

---

## 🔌 API Endpoints

**Live URL:** `https://ecommerce-backend-fastapi.onrender.com`

### 🧾 Products API

#### ➕ POST /products
```json
{
  "name": "Puma Classic Sneakers",
  "price": 2999.00,
  "sizes": [
    { "size": "UK 8", "quantity": 20 },
    { "size": "UK 9", "quantity": 15 }
  ]
}
```

#### 📄 GET /products
Query Parameters:
- `name`
- `size`
- `limit`
- `offset`

Response:
```json
{
  "data": [
    {
      "id": "66b0123abcde123456fghij",
      "name": "Puma Classic Sneakers",
      "price": 2999.00
    }
  ],
  "page": {
    "next": 10,
    "limit": 0,
    "previous": -10
  }
}
```

---

### 📦 Orders API

#### ➕ POST /orders
```json
{
  "userId": "user_abc_789",
  "items": [
    { "productId": "66b0123abcde123456fghij", "qty": 1 }
  ]
}
```

#### 📄 GET /orders/{userId}
Response:
```json
{
  "data": [
    {
      "id": "order_xyz_456",
      "items": [
        {
          "productDetails": {
            "name": "Puma Classic Sneakers",
            "price": 2999.00
          },
          "qty": 1
        }
      ],
      "total": 2999.00
    }
  ],
  "page": {
    "next": 10,
    "limit": 0,
    "previous": -10
  }
}
```

---

## 🛠️ Local Development Setup

```bash
git clone https://github.com/AbhinavRai2004/ecommerce-backend-fastapi
cd ecommerce-backend-fastapi

# .env file
MONGODB_URL=mongodb+srv://<username>:<password>@cluster.mongodb.net/yourDatabaseName

# Create virtual env and install dependencies
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run FastAPI app
uvicorn app.main:app --reload
```

Visit: `http://127.0.0.1:8000/docs` to test with Swagger UI.

---

<p align="center">
Built with ❤️ and a lot of ☕ by <strong>Abhinav Rai</strong>.
</p>
