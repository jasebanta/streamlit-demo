
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "Kynisca World"}

async def send_backend_metric(event_name):
    pass