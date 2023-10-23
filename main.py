from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def extract_info(request: Request):

    referer = request.headers.get("Referer")
    
    agent = request.headers.get("User-Agent")
    
    from user_agents import parse
    user_agent_info = parse(agent)
    browser = user_agent_info.browser.family
    device = user_agent_info.device.family

    info = {
        "Referer": referer,
        "Browser": browser,
        "Device": device,
    }

    return JSONResponse(content=info)


