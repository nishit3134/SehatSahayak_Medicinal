import streamlit as st

st.title("⚕️🏥Welcome to Sehatसहायक")

col1, col2 = st.columns(2,gap="large")

with col1:
   st.image('hero.png', width=400)
with col2:
   st.text(" ")
   st.text(" ")
   st.text(" ")
   st.header("Revolutionizing Healthcare")
   st.write("Experience healthcare on your terms with SehatSahayak. Our online platform connects you with qualified medical experts, providing convenient and confidential assistance whenever and wherever you need it. Your health, on your finger tips.")


hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)