import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image

st.header("Teilbarkeitsregeln und Primzahlen")
image_url = "https://imageshack.com/i/pmpxMV2Qj"
st.image(image_url)

st.markdown("Eine **Primzahl** ist eine natürliche Zahl, die **genau zwei natürliche Teiler** hat.)
st.markdown("Die ersten zehn Primzahlen sind:")
st.latex(r"""\mathrm{2, \: 3, \: 5, \: 7, \: 11, \: 13, \: 17, \: 19, \: 23, \:, 29, \: ...}""")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Teilbarkeitsregeln](https://www.learningsnacks.de/share/249456/299dc33dbfdf78fbddc02610cfcfcffabaceb33d)")
