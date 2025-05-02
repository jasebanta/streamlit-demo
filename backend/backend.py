
from fastapi import FastAPI
import httpx
import random
from pydantic import BaseModel
from typing import List, Dict, Any

class GA4Event(BaseModel):
    name: str
    params: Dict[str, Any] = {}
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "Kynisca World"}

# @app.post("/GA4track")
# async def send_to_ga4(events: List[GA4Event]):
#     url = f'https://www.google-analytics.com/mp/collect?measurement_id={MEASUREMENT_ID}&api_secret={API_SECRET}'

#     payload = {
#         "client_id": f"{random.randint(1000000000,9999999999)}.{random.randint(1000000000,9999999999)}",
#         "events": [event.dict() for event in events]
#     }

#     async with httpx.AsyncClient() as client:
#         response = await client.post(url, json=payload)

#     return {"status_code": response.status_code, "response_text": response.text}