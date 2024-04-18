import streamlit as st
import requests

st.title("Kynisca Innovation Center")

st.divider()

pp = """Privacy Policy
Version 0.0.1
April 17, 2024
This Application by Kynisca International, LTD (“Kynisca”) is still under development. Information collected by the Application or company will be used solely for development purposes and will not carry over for any commercial purpose. The information provided to us will be available internally to Kynisca employees and any contracted individuals and companies (“Contractors”) working with Kynisca on the development of the Application. Users who choose to share their information with Kynisca during the development phase will not have any data shared publicly but should otherwise have no expectations of privacy. Upon completion of development, all personal information including personally identifiable information (“PII”), personal health information (“PHI”), and data history will be permanently deleted and no backup copy shall be retained.
None of the data collected during the development phase of the Application will be sold, leased, shared, posted, or otherwise made available to any individual or organization outside of Kynisca and our Contractors.
Kynisca reserves the right to modify our Privacy Policy at any time. Upon completion of the development of the Application, a new Privacy Policy will be posted and this one will no longer be valid. If at any time, the user (“You”) disagrees with the policy, you should stop using the Application. User data will be deleted upon the completion or termination of the development phase of the Application."
"""
st.write(pp)