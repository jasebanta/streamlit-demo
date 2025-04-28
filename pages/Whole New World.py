import streamlit as st

GA_MEASUREMENT_ID = "G-5KCQSGDVVY"  # your GA4 measurement ID

# Inject the Google Analytics tracking script
st.markdown(
    f"""
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{GA_MEASUREMENT_ID}');
    </script>
    """,
    unsafe_allow_html=True,
)

st.title("Hello world!")