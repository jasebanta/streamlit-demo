import streamlit as st
from datetime import datetime as dt
import secrets
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Individual Consent",
    layout="wide"
)
st.title("Individual Consent")

# ga_code = """
# <!-- Google tag (gtag.js) -->
# <script async src="https://www.googletagmanager.com/gtag/js?id=G-5KCQSGDVVY"></script>
# <script>
#   window.dataLayer = window.dataLayer || [];
#   function gtag(){dataLayer.push(arguments);}
#   gtag('js', new Date());

#   gtag('config', 'G-5KCQSGDVVY');
# </script>
# """
# st.markdown(ga_code, unsafe_allow_html=True)



# gtag_script = """
# <script async src="https://www.googletagmanager.com/gtag/js?id=G-R0ZPWFNCRW"></script>
# <script>
#   window.dataLayer = window.dataLayer || [];
#   function gtag(){{dataLayer.push(arguments);}}
#   gtag('js', new Date());
#   gtag('config', 'G-R0ZPWFNCRW');
# </script>
# """

# components.html(gtag_script, height=0, width=0)
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

st.session_state.page_loadtime = random.randint(1,5)
track_page_view(user_id=st.session_state.get("email") or "None", page="Individual Consent", load_time = st.session_state.page_loadtime)
###############################################################################

st.divider() #--------------------------------------------
@st.dialog("Email individual")
def email(item):
    st.write(f"Generating token and email for {item}")
    coshie_id = st.text_input("COSHIE ID")
    if st.button("Submit"):
        st.session_state.email = {"coshie_id": coshie_id, "token": secrets.token_hex(8)}
        st.rerun()

if "email" not in st.session_state:
    st.write("Generate email to gather consent:")
    if st.button("Generate"):
        email("Person")
else:
    with st.container(border=True):
        st.write(
            f"Dearest Gentle Reader, your COSHIE ID is **{st.session_state.email["coshie_id"]}**, and your token is **{st.session_state.email["token"]}**"
        )

st.divider() #--------------------------------------------

# Func to submit
def update_consent(data):
    pass

with st.form("consent_form"):
    st.write("### Consent Form")
    with st.expander("Demographic", expanded=False):
        st.markdown("""
            Demographic data refers to the statistical characteristics of populations, 
                    especially those used to identify segments of the population. 
                    It provides a snapshot of "who" people are. \n
                    Examples:
                        Age - The numerical age of an individual.
                        Gender - The biological sex or gender identity of an individual.
                        Race/Ethnicity - The racial or ethnic background of an individual.
                        Geographic Location - The place where an individual lives, such as their address, city, or country.
                        Socioeconomic Status - Factors like income, education level, and occupation.
                    """
        )
        demographic_consent = st.checkbox("I have read and agree to the terms above", key="demographic_consent")
    with st.expander("Health Data", expanded=False):
        st.markdown("""
            Health data refers to information related to an individual's or a population's health status. 
                    It provides a picture of "how" healthy people are. \n
                    Examples:
                        Medical Diagnoses - Records of diagnosed diseases or conditions (e.g., diabetes, hypertension).
                        Vital Signs - Measurements like blood pressure, heart rate, and temperature.
                        Medical History - Past illnesses, surgeries, and treatments.
                        Laboratory Results - Data from blood tests, urine tests, and other diagnostic procedures.
                        Health Behaviors - Information about lifestyle choices that affect health, such as smoking, diet, and exercise.
                    """
        )
        health_consent = st.checkbox("I have read and agree to the terms above", key="health_consent")


    cols = st.columns([0.5,0.5])
    with cols[0]:
        first_name = st.text_input("Enter your first name:", key="first_name")
    with cols[1]:
        Last_name = st.text_input("Enter your last name:", key="lastname")
    coshie_id = st.text_input("Enter your COSHIE ID:", key="coshie_id")
    token = st.text_input("Enter your token:", key="token")
    date = st.write(f"Timestamp: {dt.now()}")

    data = {
        "first_name": first_name,
        "last_name": Last_name,
        "consent": {
            "demographic_consent": demographic_consent,
            "health_consent": health_consent
            },
        "coshie_id": coshie_id,
        "token": token
    }

    submitted = st.form_submit_button(
        "Submit"
    )

    if submitted:
        update_consent(data)
        st.write("Submitted")

st.divider() #--------------------------------------------
st.write("Individual Consent Storage")
st.json(data)