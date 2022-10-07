import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Weapon Fire Rate")

df = st.session_state["df"]

st.title("Weapon Fire Rate")

st.subheader("Which Weapon has the highest Fire Rate?")
df_fr = df[["Name", "Weapon Type", "Fire Rate"]].sort_values(by="Fire Rate", ascending=True)
st.dataframe(df_fr, use_container_width=True)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Below Line Chart shows Increase of Fire Rate as we move towards SMG's")

fig, ax = plt.subplots(1, 1)
ax.plot(df_fr["Name"], df_fr["Fire Rate"])
ax.set_xlabel("Weapon Name")
ax.set_ylabel("Fire Rate")
plt.xticks(rotation=45)
st.pyplot(fig)