import streamlit as st
import streamlit.components.v1 as components

GA_MEASUREMENT_ID = "G-5KCQSGDVVY"  # your GA4 measurement ID

# Remove this entire block:
# st.markdown(
#     f"""
#     #     <script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
#     <script>
#       window.dataLayer = window.dataLayer || [];
#       function gtag(){{dataLayer.push(arguments);}}
#       gtag('js', new Date());
#       gtag('config', '{GA_MEASUREMENT_ID}');
#     </script>
#     """,
#     unsafe_allow_html=True,
# )
components.html(
    """
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-5822N93W');</script>
    <!-- End Google Tag Manager -->
    """,
    height=0, width=0
)

st.title("Hello world!")

components.html(
    """
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5822N93W"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
    """,
    height=0, width=0
)