# 📺 Streaming Analytics: Predictive Strategies for Retention & Engagement

## 🧠 The Business Case
In the cut-throat world of digital streaming, data is the difference between "getting it right" and losing your audience to the competition. This project isn't just about "crunching numbers"; it's about converting user behaviour into **actionable insights**.

My approach here was to treat every row of data with the professional "care and kit" it deserves. By applying **Machine Learning** to anticipate market shifts, I've focused on ensuring the user experience remains the primary engine for revenue growth. I'm not just looking at the "what," but the "why" behind the data.

## 🎯 The Challenge: Business Questions
To make this project truly "fit for purpose," I’ve set out to tackle five critical pillars that define the success of any streaming platform:

1.  **Churn Prediction:** Which users are most likely to "call it a day" and cancel?
2.  **Engagement Drivers:** Which content genres actually keep viewers glued to their screens?
3.  **Upgrade Patterns:** Can behavioural habits predict when a user is "chuffed" enough to move to a Premium plan?
4.  **Retention Segments:** Which customer cohorts are the "bread and butter" of our Lifetime Value (LTV)?
5.  **Predictive Strategy:** How can predictive analytics "lend a hand" in sharpening our recommendation engines?

## 🏗️ Strategic Data Management & Architecture
For this project, I’ve implemented a professional data pipeline that prioritises efficiency and security:

*   **Data Segregation:** I’ve opted for a segregated folder structure to maintain a "ship-shape" environment. All raw, sensitive files are stored in `data/`, while the anonymised, production-ready outputs are directed to `data/processed/`. This ensures data lineage remains clear and audit-ready.
*   **The Parquet Standard:** I transitioned the refined layer to the **Apache Parquet** format. Dealing with 50,000 records, this is a strategic call: Parquet’s columnar storage is far more **nippy** for Machine Learning, preserves the schema perfectly, and is significantly lighter on storage.

## 🛠️ Tech Stack & Methodology
I've utilised the **Python** ecosystem to build a solution that is both robust and scalable:
*   **Storage & Schema:** `Apache Parquet` & `PyArrow`
*   **Analysis & Wrangling:** `Pandas` & `NumPy`
*   **Strategic Visualisation:** `Plotly` & `Seaborn`
*   **Artificial Intelligence:** `Scikit-Learn` (Classification & Clustering models)

> **🔒 A Note on Data Privacy & Governance:**
> Privacy is "top of mind" here. This project implements a rigorous layer of anonymisation. All names, addresses, and personal identifiers have been "binned" or replaced with cryptographic keys. This ensures the analysis focuses strictly on **mass patterns**, staying well within the lines of proper data governance and ethics—essential for any work involving public-facing or sensitive sectors.

---
**Developed by [Paulo Faria]**
*Turning raw data into a "spot of" competitive intelligence.*