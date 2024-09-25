# Multiple Disease Prediction 🩺💻

![Diseases](https://img.shields.io/badge/Disease-Prediction-red) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green)

## 📚 Overview

The **Multiple Disease Prediction Model** is designed to predict the likelihood of various diseases such as heart disease, diabetes, and Parkinson's disease based on patient health parameters. Using machine learning algorithms, this model aids in early detection and diagnosis of multiple conditions.

### 🎯 Objective
To create a single machine learning model capable of predicting multiple diseases based on medical records and clinical data.

## 📂 Project Structure

```
multiple-disease-prediction/
├── data/
│   ├── heart_disease.csv      # Dataset for heart disease
│   ├── diabetes.csv           # Dataset for diabetes
│   ├── parkinsons.csv         # Dataset for Parkinson's disease
├── notebooks/
│   ├── data_analysis.ipynb    # EDA and data analysis
│   ├── model_building.ipynb   # Model development and evaluation
├── app.py                     # Streamlit app for multiple disease prediction
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 🚀 Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/multiple-disease-prediction.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd multiple-disease-prediction
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## ⚙️ Model Building Process

### 1. Data Preprocessing 🧹
- Clean and preprocess datasets from various medical records.
- Handle missing values, standardize data, and encode categorical features where necessary.

### 2. Feature Engineering 🛠️
- Extract important features like blood pressure, glucose levels, heart rate, and more from the datasets.

### 3. Model Training 🤖
The model was trained using multiple algorithms to predict different diseases:
- **Logistic Regression**
- **Random Forest**
- **SVM**
- **K-Nearest Neighbors (KNN)**

### 4. Model Evaluation 🏅
Each model was evaluated individually for different diseases:

- **Heart Disease Prediction Accuracy:** 85%
- **Diabetes Prediction Accuracy:** 90%
- **Parkinson's Disease Prediction Accuracy:** 88%

## 🖥️ Demo

You can interact with the **Multiple Disease Prediction Model** using the Streamlit app:

https://multiple-disease-prediction-model-pd7ivqnpxerxsfmepq5fdg.streamlit.app/

## 🛠️ Technologies Used

- **Python 3.8+**
- **Pandas, Numpy** for data analysis
- **Scikit-learn** for machine learning models
- **Matplotlib, Seaborn** for data visualization
- **Streamlit** for the web interface

## 📊 Model Performance

| Disease                | Algorithm               | Accuracy |
|------------------------|-------------------------|----------|
| Heart Disease           | Logistic Regression     | 85%      |
| Diabetes                | Random Forest           | 90%      |
| Parkinson's Disease     | SVM                     | 88%      |

## 🤝 Contributing

Contributions are welcome! If you find any issues or want to enhance the model, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss your ideas.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

> 🔗 **References**:
> - [Pandas Documentation](https://pandas.pydata.org/)
> - [Scikit-learn Documentation](https://scikit-learn.org/stable/)
> - [Streamlit Documentation](https://docs.streamlit.io/)
