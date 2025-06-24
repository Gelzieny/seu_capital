from fastapi import FastAPI

# 1. Crie uma instância do FastAPI
app = FastAPI(
    title="Seu capital",
    description="Uma API para gerenciar suas receitas e despesas pessoais.",
    version="0.1.0",
)


@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à API de Controle Financeiro!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("manage:app", host="0.0.0.0", port=8000, reload=True)
