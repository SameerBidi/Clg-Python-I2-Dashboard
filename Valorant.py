from turtle import pd
from matplotlib.pyplot import title
import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(page_title="My Page Title")

st.title("Valorant Weapon Stats Explorer")

val_image = Image.open("static/images/valorant.jpg")
st.image(val_image, caption="Valorant")

st.markdown("**Valorant** is a 5v5 character-based tactical FPS where precise gunplay meets unique agent abilities.")

st.subheader("In this Web-App we are going to explore and analyze the Weapon Stats")

df = pd.read_csv("static/datasets/valorant-stats.csv")

st.session_state["df"] = df