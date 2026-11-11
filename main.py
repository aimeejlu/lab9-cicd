from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def raiz():
    return {"status": "ok", "mensagem": "API FastAPI no ar"}


@app.get("/health")
def health():
    return {"status": "healthy"}