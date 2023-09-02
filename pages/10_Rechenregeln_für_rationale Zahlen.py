import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image


st.header("Rechenregeln für rationale Zahlen")
image_url = "https://imageshack.com/i/pnib4l2lj"
st.image(image_url)
st.write("")
st.write("")
image_url = "https://imageshack.com/i/popReS1bj"
st.image(image_url)
st.write("")
st.write("")
image_url = "https://imageshack.com/i/pmUiiUbWj"
st.image(image_url)
st.write("")
st.write("")
image_url = "https://imageshack.com/i/pmkekyckj"
st.image(image_url)
st.write("")
st.write("")
image_url = "https://imageshack.com/i/pnKESB65j"
st.image(image_url)
st.write("")
st.write("")
image_url = "https://imageshack.com/i/pnYUXQiSj"
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
    st.markdown("[Kürzen und Erweitern von Brüchen](https://www.learningsnacks.de/share/251533/a1046b648696ab110cfe4c3df90cd6c525684b3d)")

col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Addieren und Subtrahieren von Brüchen](https://www.learningsnacks.de/share/251550/e68247cb48b7c134df22a4afe866edd649bfc993)")

col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Multiplizieren und Dividieren von Brüchen](https://www.learningsnacks.de/share/251570/da0479fa4b4a1c0081e897fcc8f08ebdf30c925a)")

