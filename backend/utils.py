import httpx
import random
from pydantic import BaseModel
from typing import List, Dict, Any
import streamlit as st
import pprint as p

class GA4Event(BaseModel):
    name: str
    params: Dict[str, Any] = {}


class GA4:
    @staticmethod
    def send_event(user_id: str, user_properties: dict, events: List[GA4Event]):
        url = f'https://www.google-analytics.com/mp/collect?measurement_id={st.secrets["GA4"].MEASUREMENT_ID}&api_secret={st.secrets["GA4"].API_SECRET}'

        payload = {
            # "client_id": f"{random.randint(1000000000,9999999999)}.{random.randint(1000000000,9999999999)}",
            "client_id": "9147457264.7594690140",
            # "client_id": st.session_state['session_id'],
            "user_id": user_id,
            "user_properties": user_properties,
            "events": [event.model_dump() for event in events],
            
        }
        # print(url)
        p.pprint(payload)

        with httpx.Client() as client:
            headers = {'Content-Type': 'application/json'}
            response = client.post(url, json=payload, headers=headers)

        print({"status_code": response.status_code, "response_text": response.text})