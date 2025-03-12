# from fastapi import FastAPI
# from app.routes.math_routes import router

# app = FastAPI(
#     title="Math API",
#     description="API RESTful para operações matemáticas (soma e média)",
#     version="1.0.0",
#     docs_url="/docs",
#     redoc_url="/redoc"
# )

# # Inclui as rotas
# app.include_router(router, prefix="/math", tags=["Math Operations"])

# # Health Check
# @app.get("/", tags=["Health Check"])
# def root():
#     return {"message": "Math API is running!"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
 

import os
import uvicorn
from fastapi import FastAPI
from app.routes.math_routes import router

app = FastAPI(
    title="Math API",
    description="API RESTful para operações matemáticas (soma e média)",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Inclui as rotas
app.include_router(router, prefix="/math", tags=["Math Operations"])

# Health Check
@app.get("/", tags=["Health Check"])
def root():
    return {"message": "Math API is running!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Render define automaticamente a porta na variável de ambiente PORT
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
 