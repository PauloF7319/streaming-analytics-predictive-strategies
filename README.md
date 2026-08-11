📺 Streaming Analytics – Predictive Strategies for Retention & Engagement
Business Context

This project explores how customer behaviour data can be used to understand engagement, customer retention and subscription patterns in a streaming environment.

The main objective was to build a data and machine learning workflow that could help answer practical business questions rather than focusing only on the technical aspects of the models.

The project looks at:

Which users are more likely to cancel their subscriptions?
Which content genres are associated with higher engagement?
Can user behaviour help identify customers likely to upgrade to a Premium plan?
Which customer groups show stronger retention characteristics?
How can predictive analytics support better retention and recommendation strategies?

🎯 Project Scope
I focused on building an end-to-end analytical workflow, from the original data through data preparation, analysis and predictive modelling.

The project was intentionally kept focused on the main business questions. Instead of trying to optimise every possible aspect of the models, I concentrated on building a reliable pipeline, maintaining clear data lineage and making sure that the results could be properly analysed.

Some areas, such as extensive hyperparameter optimisation and more advanced statistical comparisons, were left as possible future improvements.

🕵️ Model Validation and Data Quality
One of the most useful parts of this project was discovering that the first model results were not reliable.

The initial model achieved 100% accuracy, which immediately raised a question: was the model actually learning useful patterns, or was something wrong with the data?

After investigating the features, I identified data leakage. For example, days_since_last_watch was closely related to the target outcome and was allowing the model to obtain information that would not realistically be available at the required prediction stage.

I also found an issue in the original data mapping. Status values from the source CSV files were being interpreted incorrectly during ingestion, which affected the distinction between cancelled and active users.

After correcting the data mapping, isolating the appropriate features and applying class balancing with class_weight='balanced', the model accuracy stabilised at 82.15%.

For me, this was an important part of the project because it demonstrated that a high accuracy score is not necessarily a good result. Understanding why a model produces a result is just as important as the result itself.

🏗️ Data Pipeline and Architecture
The project uses a structured data workflow to separate the original data from the processed datasets.

Raw files are kept in the data/ directory, while processed and anonymised datasets are stored in data/processed/.

This separation makes it easier to understand the data lineage and reproduce the processing steps.

I also converted the processed data to Apache Parquet using PyArrow. With approximately 50,000 records, this provided a more efficient format for analytical and machine learning workflows while preserving the dataset schema.

🔐 Data Governance and Privacy
Privacy was also considered as part of the data preparation process.

Before data reaches the processed stage:

User_ID values are pseudonymised using SHA-256 hashing.
Names, email addresses, telephone numbers and addresses are removed.
Only the behavioural information required for the analysis is retained.

These practices were implemented to reduce the exposure of personally identifiable information and to follow principles aligned with UK GDPR.

🛠️ Technology Stack
Data Processing
Python
Pandas
NumPy
PyArrow
Apache Parquet
Data Analysis and Visualisation
Plotly
Seaborn
Machine Learning
Scikit-learn
Random Forest Classification

🚀 Future Improvements
Possible next steps include:

Further model optimisation and hyperparameter tuning
Additional evaluation metrics such as precision, recall and ROC-AUC
Testing alternative machine learning algorithms
Expanding the retention and engagement analysis
Improving pipeline monitoring and logging
Exploring deployment options

🧠 What I Learned
The most important lesson from this project was that building a machine learning model is only one part of the problem.

The quality of the data, the definition of the target, the features used for prediction and the way the results are validated can have a much greater impact than simply choosing a more sophisticated algorithm.

The discovery of data leakage was particularly valuable because it forced me to investigate why the model was performing so well instead of simply accepting the initial accuracy score.

This project helped me strengthen my understanding of data preparation, data quality, machine learning validation, privacy and the importance of building reliable analytical pipelines.

Developed by [Paulo Faria]
Turning raw data into a "spot of" competitive intelligence.
