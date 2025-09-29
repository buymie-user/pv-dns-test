from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Python 3.13 API!"}

@app.get("/ping")
def ping():
    return {"status": "ok"}
