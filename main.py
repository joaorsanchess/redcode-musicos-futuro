from fastapi import FastAPI

app = FastAPI(title="RedCode API")

@app.get("/")
def read_root():
    return {"status": "MVP Ativo", "security": "JWT ready"}