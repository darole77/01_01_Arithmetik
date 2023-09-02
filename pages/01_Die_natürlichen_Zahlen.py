import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image

st.header("Die natürlichen Zahlen $$\mathbb{N}$$")
st.markdown("Das Zählen ist die grundlegendste mathematische Tätigkeit und stand vermutlich auch im historischen Kontext am Anfang der Mathematik. Ausgehend von der Einheit (die Zahl $$\small{1}$$) entstehen durch fortlaufendes Hinzufügen weiterer Einheiten die so genannten natürlichen Zahlen $$\small{1, 2, 3, 4, 5, …}$$")
    
image_url = "https://imageshack.com/i/pm5BDdqup"
st.image(image_url)
       
st.markdown("Die Menge der natürlichen Zahlen wird in der Mathematik mit dem Symbol N bezeichnet und man schreibt: ")
st.latex(r"\mathbb{N} = \lbrace 1; 2; 3; 4; 5; ... \rbrace")
st.markdown("Dabei symbolisieren die drei Punkte $$„…“$$, dass es immer in dieser Form weitergeht, ohne jemals abzubrechen. Die natürlichen Zahlen lassen sich als Punkte am so genannten Zahlenstrahl veranschaulichen. Die Zahl 0 wird normalerweise nicht zu den natürlichen Zahlen gezählt. Möchte man die Zahl 0 dabeihaben, so schreibt man in der Regel: ")
st.latex(r"\mathbb{N}_{0} = \lbrace 1; 2; 3; 4; 5; ... \rbrace")
    
st.markdown("Die natürlichen Zahlen lassen sich am so genannten 'Zahlenstrahl' darstellen: ")
image_url = "https://imageshack.com/i/pomGWAZ5p"
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
    st.markdown("[Die natürlichen Zahlen](https://www.learningsnacks.de/share/249432/c7b260eb380b35c7fa7b6072f4e2767f1a45bab3)")


