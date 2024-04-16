import streamlit as st
import requests

st.write("Hello World")

st.divider()

a = st.slider("question1", min_value=1, max_value=100, step = 1)

if a > 10:
    import streamlit as st
    import numpy as np

    with st.chat_message("user"):
        st.write("Hello 👋")
        st.line_chart(np.random.randn(30, 3))

data = requests.get("http://localhost:8000")
st.write(data.content)