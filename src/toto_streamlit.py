import streamlit as st
from fibonacci import Fibonacci

fibonacci = Fibonacci()
fibbo = Fibonacci().fibbo

st.title("TP IA 2 - Streamlit")
st.write("Bienvenue dans l'application Streamlit pour le TP IA 2 !")
i = st.slider("Sélectionnez un nombre", 0, 100, 1)
st.write(f"Vous avez sélectionné le nombre : {i}")
st.write(f"La suite de Fibonacci pour {i} est : {fibbo(i)}")   

