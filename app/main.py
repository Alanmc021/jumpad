from fastapi import FastAPI
from app.routes import math_routes

app = FastAPI(
    title="Math API",
    description="API RESTful para operações matemáticas (soma e média)",
    version="1.0.0"
)

# Inclui as rotas da API
app.include_router(math_routes.router, prefix="/math", tags=["Math Operations"])

# Rota raiz para verificar se a API está rodando
@app.get("/", tags=["Health Check"])
def root():
    return {"message": "Math API is running!"}

# Executar o servidor apenas se o script for chamado diretamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
 