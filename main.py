import streamlit as st

# creating containers
header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
modeTraining = st.beta_container()

with header:
	st.Title('Crime Classification')