import streamlit as st
import streamlit.components.v1 as components

# Google Analytics Tracking Code
GA_JS = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-9663NCZLHD"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-9663NCZLHD');
</script>
"""

# Embed the Google Analytics script in the app
components.html(GA_JS)
