import streamlit as st
import matplotlib.pyplot as plt
import dataset_reader

st.set_page_config(page_title="Weapon Types")

df = dataset_reader.get_valorant_stats_data()

st.title("Weapon Types")

st.subheader("How many Weapon Types do we have?")
df_wt = df["Weapon Type"].value_counts().rename_axis("Weapon Type").reset_index(name="Count")
st.dataframe(df_wt, use_container_width=True)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Below Pie Chart shows (%) Percentage share of each Weapon Type")
st.markdown("It gives you a good idea about which Weapon Type has the most amount of Weapons")

fig, ax = plt.subplots(1, 1)
_, _, per_labels = ax.pie(x=df_wt["Count"], labels=df_wt["Weapon Type"], autopct="%1.0f%%", pctdistance=0.7, labeldistance=1.2)
for i in range(len(per_labels)):
  per_labels[i].set_color("white")
st.pyplot(fig)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Weapon Types and their Fire Rate")
df_wt_fr = df.groupby("Weapon Type")[["Weapon Type", "Fire Rate"]].agg("mean").sort_values(by="Fire Rate", ascending=False).reset_index()
st.dataframe(df_wt_fr, use_container_width=True)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Below Bar Chart shows that SMG's have the most Fire Rate")

fig, ax = plt.subplots(1, 1)
ax.bar(df_wt_fr["Weapon Type"], df_wt_fr["Fire Rate"])
ax.set_xlabel("Weapon Type")
ax.set_ylabel("Fire Rate")
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Weapon Types and their Cost")
df_wt_pr = df.groupby("Weapon Type")[["Weapon Type", "Price"]].agg("sum").sort_values("Price", ascending=False).reset_index()
st.dataframe(df_wt_pr, use_container_width=True)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Below Bar Chart shows that Rifle's are more expensive")

fig, ax = plt.subplots(1, 1)
ax.bar(df_wt_pr["Weapon Type"], df_wt_pr["Price"])
ax.set_xlabel("Weapon Type")
ax.set_ylabel("Price")
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Weapon Types and their Magazine Capacity")
df_wt_mc = df.groupby("Weapon Type")[["Weapon Type", "Magazine Capacity"]].agg("sum").sort_values("Magazine Capacity", ascending=False).reset_index()
st.dataframe(df_wt_mc, use_container_width=True)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Below Bar Chart shows that Heavy's have more Magazine Capacity")

fig, ax = plt.subplots(1, 1)
ax.bar(df_wt_mc["Weapon Type"], df_wt_mc["Magazine Capacity"])
ax.set_xlabel("Weapon Type")
ax.set_ylabel("Magazine Capacity")
plt.xticks(rotation=45)
st.pyplot(fig)