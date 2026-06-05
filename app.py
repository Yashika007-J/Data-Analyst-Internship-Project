import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("UAC.csv")
df.columns = ["Date","CBP_Apprehended","CBP_Custody",
              "CBP_Transferred","HHS_Care","HHS_Discharged"]
df["Date"] = pd.to_datetime(df["Date"], format="mixed")
df = df.sort_values("Date").reset_index(drop=True)

st.title("Care Transition Efficiency Dashboard")
st.subheader("Children in HHS Care Over Time")

fig, ax = plt.subplots(figsize=(12,5))
ax.plot(df["Date"], df["HHS_Care"], color="blue")
ax.set_xlabel("Date")
ax.set_ylabel("Count")
ax.grid(True)
st.pyplot(fig)