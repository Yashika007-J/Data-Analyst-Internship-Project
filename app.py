import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("UAC.csv")
df.columns = ["Date","CBP_Apprehended","CBP_Custody",
              "CBP_Transferred","HHS_Care","HHS_Discharged"]
df["Date"] = pd.to_datetime(df["Date"], format="mixed")
df = df.sort_values("Date").reset_index(drop=True)

for col in ["CBP_Apprehended","CBP_Transferred","HHS_Care","HHS_Discharged"]:
    df[col] = df[col].astype(str).str.replace(",","").str.strip()
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

df["Transfer_Efficiency"] = df["CBP_Transferred"] / df["CBP_Apprehended"].replace(0,1)
df["Discharge_Effectiveness"] = df["HHS_Discharged"] / df["HHS_Care"].replace(0,1)

# Sidebar
st.sidebar.title("🔧 Filters")
st.sidebar.markdown("Use filters to explore specific time periods.")
start_date = st.sidebar.date_input("📅 Start Date", df["Date"].min())
end_date = st.sidebar.date_input("📅 End Date", df["Date"].max())

mask = (df["Date"] >= pd.Timestamp(start_date)) & (df["Date"] <= pd.Timestamp(end_date))
filtered = df[mask]

# Title
st.title("Care Transition Efficiency & Placement Outcome Dashboard")
st.markdown("This dashboard analyzes how efficiently children move through the UAC care pipeline — from CBP custody to HHS care to sponsor placement.")

# KPIs
st.subheader("Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Transfer Efficiency", 
            f"{filtered['Transfer_Efficiency'].mean():.2f}",
            help="Transfers ÷ Apprehensions. Value > 1 means system is clearing backlog.")
col2.metric("Avg Discharge Rate", 
            f"{filtered['Discharge_Effectiveness'].mean():.2f}",
            help="Discharges ÷ HHS Care load. Higher = better placement outcomes.")
col3.metric("Total Records", len(filtered))

# Chart 1
st.subheader("Children in HHS Care Over Time")
st.markdown("Shows the total number of children under HHS care each day. A rising trend indicates system overload.")
fig, ax = plt.subplots(figsize=(12,4))
ax.plot(filtered["Date"], filtered["HHS_Care"], 
        color="blue", linewidth=1.5, label="Children in HHS Care")
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("Number of Children", fontsize=12)
ax.set_title("Children in HHS Care Over Time", fontsize=14)
ax.legend()
ax.grid(True)
plt.tight_layout()
st.pyplot(fig)

# Chart 2
st.subheader("Daily Apprehensions Over Time")
st.markdown("Number of children apprehended and placed in CBP custody each day.")
fig2, ax2 = plt.subplots(figsize=(12,4))
ax2.plot(filtered["Date"], filtered["CBP_Apprehended"], 
         color="red", linewidth=1.5, label="Daily Apprehensions")
ax2.set_xlabel("Date", fontsize=12)
ax2.set_ylabel("Number of Children", fontsize=12)
ax2.set_title("Daily Apprehensions Over Time", fontsize=14)
ax2.legend()
ax2.grid(True)
plt.tight_layout()
st.pyplot(fig2)

# Chart 3
st.subheader("Transfer Efficiency Over Time")
st.markdown("Ratio of children transferred from CBP to HHS vs total apprehended. Value above 1.0 is healthy.")
fig3, ax3 = plt.subplots(figsize=(12,4))
ax3.plot(filtered["Date"], filtered["Transfer_Efficiency"], 
         color="purple", linewidth=1.5, label="Transfer Efficiency Ratio")
ax3.axhline(y=1.0, color="red", linestyle="--", label="Target (1.0)")
ax3.set_xlabel("Date", fontsize=12)
ax3.set_ylabel("Efficiency Ratio", fontsize=12)
ax3.set_title("Transfer Efficiency Over Time", fontsize=14)
ax3.legend()
ax3.grid(True)
plt.tight_layout()
st.pyplot(fig3)

# Chart 4
st.subheader("Daily Discharges Over Time")
st.markdown("Number of children successfully discharged from HHS care to a vetted sponsor each day.")
fig4, ax4 = plt.subplots(figsize=(12,4))
ax4.plot(filtered["Date"], filtered["HHS_Discharged"], 
         color="green", linewidth=1.5, label="Daily Discharges")
ax4.set_xlabel("Date", fontsize=12)
ax4.set_ylabel("Number of Children", fontsize=12)
ax4.set_title("Daily Discharges from HHS Care", fontsize=14)
ax4.legend()
ax4.grid(True)
plt.tight_layout()
st.pyplot(fig4)

# Chart 5
st.subheader("Monthly Total Apprehensions")
st.markdown("Bar chart showing total apprehensions per month — helps identify seasonal patterns and peak periods.")
filtered["Month"] = filtered["Date"].dt.to_period("M").astype(str)
monthly = filtered.groupby("Month")["CBP_Apprehended"].sum().reset_index()
fig5, ax5 = plt.subplots(figsize=(14,5))
ax5.bar(monthly["Month"], monthly["CBP_Apprehended"], 
        color="red", label="Monthly Apprehensions")
ax5.set_xlabel("Month", fontsize=12)
ax5.set_ylabel("Total Apprehensions", fontsize=12)
ax5.set_title("Monthly Total Apprehensions", fontsize=14)
ax5.legend()
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(fig5)

# Chart 6
st.subheader("Correlation Heatmap")
st.markdown("Shows how strongly each variable is related to others. Values close to 1 or -1 indicate strong correlation.")
corr = filtered[["CBP_Apprehended","CBP_Transferred",
                 "HHS_Care","HHS_Discharged",
                 "Transfer_Efficiency","Discharge_Effectiveness"]].corr()
fig6, ax6 = plt.subplots(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax6)
ax6.set_title("Correlation Heatmap of Key Metrics", fontsize=14)
plt.tight_layout()
st.pyplot(fig6)

st.success("Dashboard Complete! All charts updated based on selected date range.")
