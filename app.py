from fastapi import FastAPI
from fastapi.responses import JSONResponse
import socket
import requests


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

@app.get("/oip")
def outbound_ip():
    try:
        # Ask an external service to tell us our public IP
        ip = requests.get("https://ifconfig.me/ip", timeout=5).text.strip()
        return {"outbound_ip": ip}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

@app.get("/ifconfig")
def ifconfig_all():
    """
    Mimics 'curl https://ifconfig.me/all'
    Returns JSON with IP, location, ASN, user-agent info
    """
    try:
        headers = {"User-Agent": "curl/7.88.1"}  # mimic curl
        resp = requests.get("https://ifconfig.me/all", headers=headers, timeout=5)
        resp.raise_for_status()
        # The service returns plain text, split into lines
        info = {}
        for line in resp.text.splitlines():
            if "=" in line:
                k, v = line.split("=", 1)
                info[k.strip()] = v.strip()
        return info
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

# For local dev:  uvicorn app:app --host 0.0.0.0 --port 8000
