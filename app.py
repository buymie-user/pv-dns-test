from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "Hello from Azure Web App!"}

@app.get("/ping")
def ping():
    return JSONResponse({"ping": "pong"})

# For local dev:  uvicorn app:app --host 0.0.0.0 --port 8000
