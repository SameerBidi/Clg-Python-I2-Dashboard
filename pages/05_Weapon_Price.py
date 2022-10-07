import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Weapon Price")

df = st.session_state["df"]

st.title("Weapon Fire Rate")

st.subheader("Which Weapon has the highest Price?")
df_pr = df[["Name", "Price", "HDMG_0"]].sort_values(by="Price", ascending=True)
st.dataframe(df_pr, use_container_width=True)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Below Step Chart shows Increase of Price as we move towards more powerful Weapons")

fig, ax = plt.subplots(1, 1)
ax.step(df_pr["Name"], df_pr["Price"])
ax.set_xlabel("Weapon Name")
ax.set_ylabel("Price")
plt.xticks(rotation=45)
st.pyplot(fig)