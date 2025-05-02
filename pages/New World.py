import streamlit as st
import streamlit.components.v1 as components

# Set the page title
st.set_page_config(page_title="Streamlit with Google Analytics", layout="wide")

st.title("📊 Streamlit App with Google Analytics")

#############################################################################
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
custom_utils_path = os.path.join(current_dir, 'backend')
if custom_utils_path not in sys.path:
    sys.path.append(custom_utils_path)
    
from backend.utils import GA4, GA4Event
def track_login(user_id, debug:bool = False):
    event = GA4Event(name="login", params={
        "method": "username/password",
        "debug_mode": debug
        }
    )
    GA4.send_event(user_id = user_id, events = [event], user_properties = st.session_state.user_properties)

def track_page_view(user_id, page, load_time, debug:bool = False):
    event = GA4Event(name="page_visit", params={
        "page_name": page,
        "page_load_time": load_time,
        "debug_mode": debug
    }
  )
    GA4.send_event(user_id = user_id, events = [event], user_properties = st.session_state.user_properties)
###############################################################################

track_page_view(user_id=st.session_state.email, page="New World", load_time = st.session_state.page_loadtime)
st.write(st.session_state)