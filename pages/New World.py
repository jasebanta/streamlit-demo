import streamlit as st
import streamlit.components.v1 as components

# Set the page title
st.set_page_config(page_title="Streamlit with Google Analytics", layout="wide")

st.title("📊 Streamlit App with Google Analytics")

st.write("This is a simple Streamlit app that includes Google Analytics tracking.")

# --- Inject Google Analytics ---
GA_MEASUREMENT_ID = "G-5KCQSGDVVY"

ga4_script = f"""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_MEASUREMENT_ID}');
</script>
"""

# Render the GA script (height and width = 0 so it's invisible)
components.html(ga4_script, height=0, width=0)

# --- Main app content ---
st.write("Scroll down for more content.")
st.button("Click Me!")
