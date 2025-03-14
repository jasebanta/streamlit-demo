import streamlit as st
from datetime import datetime as dt
import secrets

st.set_page_config(
    page_title="Individual Consent",
    layout="wide"
)
st.title("Individual Consent")


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