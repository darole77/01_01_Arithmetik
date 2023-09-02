import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image

st.header("Rechenregeln für ganze Zahlen")
st.markdown("Um den Unterschied zwischen Rechenzeichen und Vorzeichen zu verdeutlichen, werden Zahlen und ihre Vorzeichen normalerweise in Klammern gesetzt.")
image_url = "https://imageshack.com/i/pmpozegDj"
st.image(image_url)
image_url = "https://imageshack.com/i/pnQ3xc2cj"
st.image(image_url)
image_url = "https://imageshack.com/i/pmHQNTRlj"
st.image(image_url)

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Rechenregeln für ganze Zahlen](https://www.learningsnacks.de/share/251220/fc605d7701749d3caf676ee3de25edb49d1dc213)")
