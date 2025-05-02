import streamlit as st
import random

# Set the page title
st.set_page_config(page_title="Streamlit with Google Analytics", layout="wide")

st.title("📊 Streamlit App with Google Analytics")

#############################################################################
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import backend.utils as GAU
import random
def track_login(user_id, debug:bool = False, user_properties = None):
    event = GAU.GA4Event(name="login", params={
        "method": "username/password",
        "debug_mode": debug
        }
    )
    GAU.GA4.send_event(user_id = user_id, events = [event], user_properties = user_properties)

def track_page_view(user_id, page, load_time, user_properties = None, debug:bool = False):
    event = GAU.GA4Event(name="page_visit", params={
        "page_name": page,
        "page_load_time": load_time,
        "debug_mode": debug
    }
  )
    GAU.GA4.send_event(user_id = user_id, events = [event], user_properties = user_properties)

track_page_view(user_id=st.session_state.get("email") or "None", page="New World", load_time = st.session_state.page_loadtime)
###############################################################################