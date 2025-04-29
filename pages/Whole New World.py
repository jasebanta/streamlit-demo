import streamlit as st
import streamlit.components.v1 as components

# --- Inject Google Analytics ---
GA_MEASUREMENT_ID = "G-5KCQSGDVVY"

ga4_script = """
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-5822N93W');</script>
<!-- End Google Tag Manager -->
"""

# Render the GA script (height and width = 0 so it's invisible)
components.html(ga4_script, height=0, width=0)

st.title("Hello, whole new world!")

body_script = """
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5822N93W"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""

# Render the GA script (height and width = 0 so it's invisible)
components.html(body_script, height=0, width=0)