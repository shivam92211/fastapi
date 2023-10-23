from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello():
    return {"Hello": "World"}

@app.get("/component/{component_id}") # path parameter
async def get_components(component_id):
    return {"component_id": component_id}

@app.get("/components/") # query parameter
async def read_component(number: int , text: str):
    return {"number": number, "text": text}


