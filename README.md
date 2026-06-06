# Care Transition Efficiency & Placement Outcome Analytics
### Unified Mentor Data Analytics Internship Project

Currently working on this!

---

## 📌 Project Overview
This project analyzes the efficiency of the U.S. Unaccompanied Alien Children (UAC) 
care pipeline using 720 days of real government data. It measures how quickly and 
effectively children move from CBP custody to HHS care to sponsor placement.

UAC_Project/
│
├── UAC.csv                    # Dataset
├── csv.ipynb                  # EDA & KPI Notebook
├── app.py                     # Streamlit Dashboard
├── report.py                  # Report generator
├── UAC_Research_Paper.docx    # Research Paper
├── UAC_Project_Report.docx    # Project Report
└── README.md                  # This file

---

## 📊 Dataset
- **Source:** U.S. Department of Health and Human Services
- **Time Period:** January 2023 – December 2025
- **Records:** 720 daily observations
- **Columns:** Date, CBP Apprehended, CBP Custody, CBP Transferred, HHS Care, HHS Discharged

---

## 🎯 Key Performance Indicators
| KPI | Formula | Meaning |
|-----|---------|---------|
| Transfer Efficiency Ratio | CBP Transferred ÷ CBP Apprehended | Speed of CBP to HHS transition |
| Discharge Effectiveness | HHS Discharged ÷ HHS Care Load | Placement success rate |
| Pipeline Throughput | (Transferred + Discharged) ÷ (Apprehended + Transferred) | Overall system movement |

---

## 🔍 Key Findings
- HHS Care peaked at **11,516 children** in December 2023
- Apprehensions dropped sharply after **January 2025**
- Average Transfer Efficiency = **1.50**
- Average Discharge Rate = **0.02**

---

## 🛠️ Tools & Technologies
- Python 3.14
- Pandas — data cleaning
- Matplotlib & Seaborn — visualization
- Streamlit — interactive dashboard
- Jupyter Notebook — EDA
- VS Code — development

---

## 🚀 How to Run Dashboard
pip install streamlit pandas matplotlib seaborn
streamlit run app.py

---

## 👩‍💻 Author
**Yashika Jandaniya**
MCA Graduate — Uttaranchal University
Unified Mentor Data Analytics Intern, 2026

## 📁 Project Structure




