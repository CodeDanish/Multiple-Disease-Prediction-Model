Multiple Disease Prediction Model


Overview:

This repository contains the implementation of a machine learning project aimed at predicting the likelihood of three major diseases: heart disease, diabetes, and Parkinson's disease. The goal is to develop models that can accurately predict the risk of these diseases based on various medical and lifestyle features. These models can assist healthcare professionals and individuals in early diagnosis and preventive care.


Features:

- Data Preprocessing: Cleaned and prepared datasets for each disease by handling missing values, encoding categorical features, and normalizing numerical data.
- Exploratory Data Analysis (EDA): Conducted EDA to identify patterns and correlations within the datasets, helping to understand the key factors that influence the risk of each disease.
- Feature Engineering: Extracted and selected the most relevant features for each disease to improve the predictive power of the models.
- Modeling: Trained separate machine learning models for predicting heart disease, diabetes, and Parkinson's disease using algorithms such as Logistic Regression, Decision Trees, Random Forest, and Support Vector Machines (SVM).
- Model Evaluation: Evaluated each model's performance using accuracy, precision, recall, F1-score, and ROC-AUC curves to ensure reliable predictions.
- Deployment: Deployed the models using Streamlit to create an interactive web application where users can input their health data and receive predictions for each disease.


Installation:

To run this project on your local machine, follow these steps:

Clone the repository:

bash

Copy code

git clone https://github.com/yourusername/multiple-disease-prediction.git

Navigate to the project directory:

bash

Copy code

cd multiple-disease-prediction

Install the required dependencies:

bash

Copy code

pip install -r requirements.txt

Run the Streamlit application:

bash

Copy code

streamlit run app.py


Usage:

- Web Application: The Streamlit web app allows users to input health and medical information such as age, blood pressure, glucose levels, and more. The app will provide a prediction for each of the three diseases (heart disease, diabetes, and Parkinson's disease) based on the input data.

- Notebooks: Explore the Jupyter notebooks provided in the repository to understand the data processing, feature selection, and model training processes for each disease prediction model.


Technologies Used:

Programming Language: Python

Libraries:
- Pandas: For data manipulation and analysis
- Scikit-learn: For machine learning model development
- XGBoost: For advanced model training and boosting
- Streamlit: For deploying the models as an interactive web application
- Matplotlib/Seaborn: For data visualization during 


Contributing:

Contributions to this project are welcome! If you would like to improve the models, add new features, or fix issues, please fork the repository, create a new branch, and submit a pull request. Ensure that your contributions follow best practices and align with the project’s objectives.


License:

This project is licensed under the MIT License. See the LICENSE file for more details.

Demo:

https://multiple-disease-prediction-model-pd7ivqnpxerxsfmepq5fdg.streamlit.app/











