import streamlit as st

#############################################################################
import streamlit as st
import os
import sys

st.write("Working dir:", os.getcwd())
st.write("Script path:", os.path.abspath(__file__))
st.write("sys.path:", sys.path)

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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
track_login(user_id=st.session_state.email, user_properties= st.session_state.user_properties)
track_page_view(user_id=st.session_state.email, page="Whole New World", load_time = st.session_state.page_loadtime)
