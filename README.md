# 📌 Jumpad - Mathematical API

This repository contains a RESTful API developed with **FastAPI** for mathematical operations such as sum and average. The project is structured to ensure scalability, modular organization, and best development practices.

---

## 🚀 Technologies Used
- **FastAPI** - High-performance web framework for APIs
- **Pydantic** - Data validation
- **Uvicorn** - Lightweight and fast ASGI server
- **Pytest** - Unit testing
- **Swagger & ReDoc** - Automatic documentation

---

## 📌 Setting Up the Environment

### 1. Clone the Repository
```bash
git clone https://github.com/Alanmc021/jumpad.git
cd jumpad
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 📌 Running the API

To start the server, use the following command:
```bash
python3 -m app.main
```
The server will start at **http://127.0.0.1:8000**

---

## 📌 API Documentation
The API provides interactive documentation with Swagger UI and ReDoc:

✅ Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  
✅ ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📌 Available Endpoints

### 1️⃣ **Sum of Numbers**
**Endpoint:**
```
POST /math/sum
```
**Request:**
```json
{
  "numbers": [1, 2, 3, 4]
}
```
**Expected Response:**
```json
{
  "result": 10
}
```

### 2️⃣ **Average of Numbers**
**Endpoint:**
```
POST /math/average
```
**Request:**
```json
{
  "numbers": [10, 20, 30]
}
```
**Expected Response:**
```json
{
  "result": 20.0
}
```

---

## 📌 Unit Tests
Tests are located in the `tests/` folder. To run them:
```bash
pytest tests/
```
This validates the creation of classes and mathematical operations.

---

## 📌 Testing via Curl
### 1️⃣ **Testing Sum:**
```bash
curl -X POST "http://127.0.0.1:8000/math/sum" \
-H "Content-Type: application/json" \
-d '{"numbers": [1, 2, 3, 4]}'
```
**Expected Response:**
```json
{"result": 10}
```

### 2️⃣ **Testing Average:**
```bash
curl -X POST "http://127.0.0.1:8000/math/average" \
-H "Content-Type: application/json" \
-d '{"numbers": [10, 20, 30]}'
```
**Expected Response:**
```json
{"result": 20.0}
```

---

## 📌 Contribution
If you wish to contribute to the project, follow these steps:
1. **Fork** the repository
2. Create a **branch**: `git checkout -b my-feature`
3. Commit your changes: `git commit -m "feat: my improvement"`
4. Push your branch: `git push origin my-feature`
5. Open a **Pull Request** 🚀

---

## 📌 License
This project is under the MIT license. Feel free to use and modify it! 😃

