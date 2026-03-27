from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI(title="What Is My IP Service")

@app.get("/")
async def root():
    return {"message": "Welcome to IP Lookup Service. Use /api/ip or /ip"}

@app.get("/api/ip")
async def get_ip_json(request: Request):
    """
    Returns the client's external IP address in JSON format
    """
    # Get the client's IP address
    client_ip = request.client.host
    
    # Check for proxy headers if behind a reverse proxy
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        client_ip = forwarded.split(",")[0].strip()
    
    return JSONResponse(content={"ip": client_ip})

@app.get("/ip", response_class=HTMLResponse)
async def get_ip_html(request: Request):
    """
    Returns the client's external IP address in a user-friendly HTML format
    """
    # Get the client's IP address
    client_ip = request.client.host
    
    # Check for proxy headers if behind a reverse proxy
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        client_ip = forwarded.split(",")[0].strip()
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My IP Address</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
            }}
            .container {{
                text-align: center;
                padding: 2rem;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #333;
            }}
            .ip {{
                color: #0066cc;
                font-size: 1.5em;
                margin: 1rem 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌐 Din publika IP-adress är</h1>
            <div class="ip">{client_ip}</div>
            <p>Your public IP address is: {client_ip}</p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
