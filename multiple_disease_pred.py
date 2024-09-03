import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu 

# Loading the saved model
diabetes_model = pickle.load(open('Diabetes_Model.sav','rb'))

heart_disease_model = pickle.load(open('Heart_Disease_Model.sav','rb'))

parkinson_disease_model = pickle.load(open('Parkinsons_Disease_Model.sav','rb'))

# Streambar for navigation
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction",['Diabetes Prediction','Heart Disease Prediction','Parkinson Prediction'], icons = ['activity','heart-pulse-fill','person'] ,default_index = 0)

# Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):

    st.title("Diabetes Prediction Model Using ML")

    # Getting the input data from user
    # columns for input field
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnencies = st.text_input("Number Of Pregnencies")

    with col2:
        Glucose = st.text_input("Glucose Level") 

    with col3:
        BloodPressure = st.text_input("BloodPressure Value") 

    with col1:
        SkinThickness = st.text_input("SkinThickness Value") 

    with col2:
        Insulin = st.text_input("Insulin Level")

    with col3:
        BMI = st.text_input("BMI Value")

    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")

    with col2:
        Age = st.text_input("Age of a person")

    # Code for prediction
    diab_diagnosis = ''

    # Button for prediction
    if st.button('Diabetes Test Result'):

        diabetes_prediction = diabetes_model.predict([[Pregnencies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if(diabetes_prediction[0]==0):
            diab_diagnosis = 'The Person is Fit and Healthy'
        else:
            diab_diagnosis = 'The Person is sufferring from Diabetes'
        
        st.success(diab_diagnosis)

if(selected == 'Heart Disease Prediction'):
    st.title("Heart Disease Prediction Model Using ML")

    # Getting the input data from user
    # columns for input field
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Enter your Age")

    with col2:
        sex = st.text_input("Enter your Sex") 

    with col3:
        cp = st.text_input("Enter chest pain type (4 values)") 

    with col1:
        trestbps = st.text_input("Enter resting blood pressure value") 

    with col2:
        chol = st.text_input("Enter serum cholestroalin mg/dl")

    with col3:
        fbs = st.text_input("Enter fast blood sugar in > 120 mg/dl")

    with col1:
        restecg = st.text_input("Enter resting ecg results value")

    with col2:
        thalach = st.text_input("Enter maximum heart rate achieved")

    with col3:
        exang = st.text_input("Enter exercise induced angina")

    with col1:
        oldpeak = st.text_input("Enter ST depression induced by exercise relative to rest value")

    with col2:
        slope = st.text_input("Enter slope of the peak exercise ST segment value")

    with col3:
        ca = st.text_input("Enter number of major vessels colored by flourosopy")

    with col1:
        thal = st.text_input("Enter thal value")

    # Code for prediction
    heart_diagnosis = ''

    # Button for prediction
    if st.button('Heart Disease Test Result'):

        heart_data_columns  = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        array = np.array(heart_data_columns, dtype=float)
        heart_prediction = heart_disease_model.predict([array])

        if(heart_prediction[0]==0):
            heart_diagnosis = 'The Person is Fit and Healthy'
        else:
            heart_diagnosis = 'The Person is sufferring from Heart Disease'
        
        st.success(heart_diagnosis)


if(selected == 'Parkinson Prediction'):
    st.title("Parkinson Prediction Model Using ML")

    # Getting the input data from user
    # columns for input field
    col1, col2, col3 = st.columns(3)

    with col1:
        Fo_Hz = st.text_input("Enter MDVP Fo(Hz) value")

    with col2:
        Fhi_Hz = st.text_input("Enter MDVP Fhi(Hz) value") 

    with col3:
        Flo_Hz = st.text_input("Enter MDVP Flo(Hz) value") 

    with col1:
        Jitter_per = st.text_input("Enter MDVP Jitter(%) value") 

    with col2:
        Jitter_Abs = st.text_input("Enter MDVP Jitter(Abs) value")

    with col3:
        RAP = st.text_input("Enter MDVP RAP value")

    with col1:
        PPQ = st.text_input("Enter MDVP PPQ value")

    with col2:
        DDP = st.text_input("Enter Jitter DDP value")
    
    with col3:
        Shimmer = st.text_input("Enter MDVP Shimmer value")

    with col1:
        Shimmer_bd = st.text_input("Enter MDVP Shimmer(bd) value")

    with col2:
        APQ3 = st.text_input("Enter Shimmer APQ3 value")

    with col3:
        APQ5 = st.text_input("Enter Shimmer APQ5 value")

    with col1:
        APQ = st.text_input("Enter MDVP APQ value")

    with col2:
        DDA = st.text_input("Enter Shimmer DDA value")

    with col3:
        NHR = st.text_input("Enter NHR value")

    with col1:
        HRN = st.text_input("Enter HRN value")

    with col2:
        RPDE = st.text_input("Enter RPDE value")

    with col3:
        DFA = st.text_input("Enter DFA value")

    with col1:
        spread1 = st.text_input("Enter spread1 value")

    with col2:
        spread2 = st.text_input("Enter spread2 value")

    with col3:
        D2 = st.text_input("Enter D2 value")

    with col1:
        PPE = st.text_input("Enter PPE value")

    # Code for prediction
    parkinson_diagnosis = ''

    # Button for prediction
    if st.button('Parkinsons Test Result'):

        parkinson_prediction = parkinson_disease_model.predict([[Fo_Hz,Fhi_Hz,Flo_Hz,Jitter_per,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_bd,APQ3,APQ5,APQ,DDA,NHR,HRN,RPDE,DFA,spread1,spread2,D2,PPE]])

        if(parkinson_prediction[0]==0):
            parkinson_diagnosis = 'The Person is Fit and Healthy'
        else:
            parkinson_diagnosis = 'The Person is sufferring from Parkinson'
        
        st.success(parkinson_diagnosis)
