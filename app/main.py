from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

# Steg 3 i uppgiften: JSON-route
@app.get("/api/ip")
def get_ip(request: Request):
    ip = request.client.host
    return {"ip": ip}

# Vidareutveckling: HTML-route
@app.get("/ip", response_class=HTMLResponse)
def get_ip_html(request: Request):
    ip = request.client.host
    return f"""
    <html>
        <body>
            <h1>Din publika IP-adress är {ip}</h1>
        </body>
    </html>
    """
