from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "Hello from Azure Web App!"}

@app.get("/ping")
def ping():
    return JSONResponse({"ping": "pong"})

@app.get("/lip")
def local_ip():
    import socket
    try:
        # Get hostname and resolve to IP
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return {"hostname": hostname, "local_ip": local_ip}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# For local dev:  uvicorn app:app --host 0.0.0.0 --port 8000
