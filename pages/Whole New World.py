import streamlit as st

#############################################################################
import backend.utils as GAU

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

def track_data_download(user_id, latency_ms, size, user_properties = None, debug:bool = False):
    event = GAU.GA4Event(name="data_exported", params={
        "latency_ms": latency_ms,
        "size": size,
        "debug_mode": debug
    }
  )
    GAU.GA4.send_event(user_id = user_id, events = [event], user_properties = user_properties)
###############################################################################

st.write("Login with Username: `jsmith` Password: `abc` OR Username: `rbriggs` Password: `def`")

import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os
import random

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'credential.yaml')

with open(config_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# stauth.Hasher.hash_passwords(config['credentials'])

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

try:
    authenticator.login()
except Exception as e:
    st.error(e)

###############################################################################
st.title(f"Welcome, {st.session_state.name}!")
role = st.selectbox(
    label="Please select your role:",
    options=st.session_state.roles
)

st.session_state.page_loadtime = random.randint(1,5)
st.session_state.user_properties = {
        "user_role": {"value": role},
        "organization": {"value": f"Organization {random.randint(1,5)}"},
        "county": {"value": f"County {random.randint(1,5)}"}
      }

st.write(f"Your page load time is: {st.session_state.page_loadtime}")
track_login(user_id=st.session_state.email, user_properties= st.session_state.user_properties, debug=True)
track_page_view(user_id=st.session_state.email, page="Whole New World", load_time = st.session_state.page_loadtime, debug=True)
# track_data_download(user_id=st.session_state.email, user_properties = st.session_state.user_properties, debug = True)

st.divider()
if st.button("Download Data"):
    lms, s = (round(random.uniform(1.0, 5.0),2), round(random.uniform(1.0, 100.0),2))
    track_data_download(
        user_id=st.session_state.email,
        latency_ms=lms,
        size=s,
        user_properties=st.session_state.user_properties,
        debug=True
    )
    st.write(f"latency_ms = {lms}, size = {s}.")