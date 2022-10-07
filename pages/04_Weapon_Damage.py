import streamlit as st
import matplotlib.pyplot as plt
import dataset_reader

st.set_page_config(page_title="Weapon Damage")

df = dataset_reader.get_valorant_stats_data()

st.title("Weapon Damage")

st.subheader("Which Weapon does the most Damage?")
df_pr = df[["Name", "HDMG_0", "BDMG_0", "LDMG_0", "HDMG_1", "BDMG_1", "LDMG_1", "HDMG_2", "BDMG_2", "LDMG_2"]]
st.dataframe(df_pr, use_container_width=True)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Below Bar Chart shows Head, Body, Leg Damage at Close range")

fig, ax = plt.subplots(1, 1)
ax.bar(df_pr["Name"], df_pr["HDMG_0"], label="Head")
ax.bar(df_pr["Name"], df_pr["BDMG_0"], label="Body")
ax.bar(df_pr["Name"], df_pr["LDMG_0"], label="Leg")
ax.set_xlabel("Weapon Name")
ax.set_ylabel("Damage")
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Below Horizontal Bar Chart shows Head, Body, Leg Damage at Medium range")

fig, ax = plt.subplots(1, 1)
ax.barh(df_pr["Name"], df_pr["HDMG_1"], label="Head")
ax.barh(df_pr["Name"], df_pr["BDMG_1"], label="Body")
ax.barh(df_pr["Name"], df_pr["LDMG_1"], label="Leg")
ax.set_xlabel("Weapon Name")
ax.set_ylabel("Damage")
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Below Scatter Chart shows Head, Body, Leg Damage at Max range")

fig, ax = plt.subplots(1, 1)
ax.scatter(df_pr["Name"], df_pr["HDMG_2"], label="Head")
ax.scatter(df_pr["Name"], df_pr["BDMG_2"], label="Body")
ax.scatter(df_pr["Name"], df_pr["LDMG_2"], label="Leg")
ax.set_xlabel("Weapon Name")
ax.set_ylabel("Damage")
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)