from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/extract-info")
async def extract_info(request: Request):
    referer = request.headers.get("Referer")
    
    user_agent = request.headers.get("User-Agent")
    
    soup = BeautifulSoup(user_agent, 'html.parser')
    
    # Extract browser and device information from the User-Agent string
    browser = soup.find("browserversion").text if soup.find("browserversion") else "Unknown"
    device = soup.find("device").text if soup.find("device") else "Unknown"

    info = {
        "Referer": referer,
        "Browser": browser,
        "Device": device,
    }

    return JSONResponse(content=info)
