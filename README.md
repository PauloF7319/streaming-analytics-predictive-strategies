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

## 🚧 Strategic Scope & Boundaries (The "Professional Reality" Check)

Executive Note: In a large scale production environment, a project of this scale would involve months of academic research. To maintain focus on delivering immediate business value and demonstrating pipeline integrity, the following strategic boundaries have been set for this portfolio:

*•*	Focus on Predictive Outcomes: I am prioritising "Deployment Ready" logic over an academic thesis comparing frequentist vs. bayesian statistics.
*•*	Pragmatic Model Selection: While I have selected robust algorithms, I am bypassing exhaustive 'Grid Search' benchmarking to focus on Data Governance and Pipeline Reliability.
*•*	Purpose Driven EDA: Every chart and analysis here is strictly tied to a Business Requirement. I am avoiding "exploration for exploration's sake" to maintain a lean, high impact analytical layer.
*•*	System Integrity vs. Hyper Tuning: The focus remains on the End to End Architecture. Chasing a 0.1% increase in accuracy is deferred in favour of ensuring a "ship shape" data lineage and auditability.

## 🎯 The Gold Standard: Accuracy & Validation 
To ensure the predictive engine is "fit for purpose" and provides reliable support for executive decision making, I have set a **95% minimum accuracy** threshold for the Machine Learning models. Achieving this "Gold Standard" is only possible through the rigorous data cleansing and feature engineering described in my pipeline, ensuring the model learns from high integrity signals, not noise.

### 🔐 Data Governance & GDPR Compliance (The "Safe Hands" Protocol)
To align with UK GDPR standards and ensure public-sector levels of data security, the pipeline implements a strict **Anonymisation Layer** before any data reaches the 'Processed' stage:

* **Pseudonymisation:** `User_ID` fields are transformed via **SHA-256 Hashing**, ensuring unique tracking for ML without exposing real user identities.
* **PII Scrubbing:** All Personally Identifiable Information (Names, Emails, Addresses) is systematically removed from the refined datasets.
* **Deep Cleaning:** Automated removal of duplicates, normalization of characters, and median-based imputation to eliminate noise and protect the **95% accuracy target**.


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

## 🔐 GDPR Compliance & Data Anonymisation To align with UK GDPR standards, this pipeline implements a strict anonymisation layer before data reaches the 'Processed' (Silver) stage.
•	User Pseudonymisation: Personal identifiers are hashed using SHA-256 protocols.
•	PII Scrubbing: Direct identifiers (Names, Emails) are systematically removed.
•	Data Minimisation: Only behavioural features relevant to Churn and Engagement are retained, ensuring the "Right to Privacy" is upheld while maintaining high quality predictive signals.


---
**Developed by [Paulo Faria]**
*Turning raw data into a "spot of" competitive intelligence.*