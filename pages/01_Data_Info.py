import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Info")

df = st.session_state["df"]

st.title("Let's get to know our data")

st.subheader("Complete Data")
st.dataframe(df, use_container_width=True)

r, c = df.shape

st.markdown(f"**The data has {r} Rows and {c} Columns**")

st.subheader("Column Details")

cols_data = pd.DataFrame({
  "Column Name" : df.columns,
  "Description": [
    "Name of the Weapon",
    "Type of the Weapon",
    "Cost of the Weapon",
    "The Rate at which the Weapon fires",
    "Wall Penetration Power of the Weapon",
    "How many bullets can the magazine of the Weapon hold",
    "Head Damage from Close Range",
    "Body Damage from Close Range",
    "Leg Damage from Close Range",
    "Head Damage from Medium Range",
    "Body Damage from Medium Range",
    "Leg Damage from Medium Range",
    "Head Damage from Max Range",
    "Body Damage from Max Range",
    "Leg Damage from Max Range"
    ]
})
st.dataframe(cols_data, use_container_width=True)