import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load model dan scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Judul aplikasi
st.markdown("""
    <h1 style='text-align: center;'>Jaya Jaya Maju Institut</h1>
    <h2 style='text-align: center;'> Prediksi Status Siswa </h2>
    <hr>
""", unsafe_allow_html=True)

# Input user
st.subheader("📝 Masukkan Informasi Siswa")
curricular_units_2nd_sem_approved = st.number_input('Curricular Units 2nd Semester Approved', min_value=0, max_value=25, value=2)
curricular_units_2nd_sem_grade = st.number_input('Curricular Units 2nd Semester Grade', min_value=0, max_value=20, value=4)
curricular_units_1st_sem_approved = st.number_input('Curricular Units 1st Semester Approved', min_value=0, max_value=30, value=4)
curricular_units_1st_sem_grade = st.number_input('Curricular Units 1st Semester Grade', min_value=0, max_value=20, value=2)
age_at_enrollment = st.number_input('Age at Enrollment', min_value=15, max_value=70, value=20)
tuition_fees_up_to_date_text = st.selectbox('Tuition Fees Up to Date', ['Yes', 'No'], index=0)
scholarship_holder_text = st.selectbox('Scholarship Holder', ['Yes', 'No'], index=1)
debtor_text = st.selectbox('Debtor', ['Yes', 'No'], index=1)
gender_text = st.selectbox('Gender', ['Female', 'Male'], index=1)

# Konversi input kategori ke nilai numerik
tuition_fees_up_to_date = 1 if tuition_fees_up_to_date_text == 'Yes' else 0
scholarship_holder = 1 if scholarship_holder_text == 'Yes' else 0
debtor = 1 if debtor_text == 'Yes' else 0
gender = 1 if gender_text == 'Male' else 0

# Buat DataFrame untuk prediksi
user_input = pd.DataFrame({
    "Curricular_units_2nd_sem_approved": [curricular_units_2nd_sem_approved],
    "Curricular_units_2nd_sem_grade": [curricular_units_2nd_sem_grade],
    "Curricular_units_1st_sem_approved": [curricular_units_1st_sem_approved],
    "Curricular_units_1st_sem_grade": [curricular_units_1st_sem_grade],
    "Tuition_fees_up_to_date": [tuition_fees_up_to_date],
    "Scholarship_holder": [scholarship_holder],
    "Gender": [gender],
    "Debtor": [debtor],
    "Age_at_enrollment": [age_at_enrollment]
})

user_input = scaler.transform(user_input)

mapping = {0: "🎗️ Siswa kemungkinan akan Graduate", 1: "⚠️ Siswa kemungkinan akan Dropout"}

if st.button("Prediksi Status 🔍"):
    # Prediksi menggunakan model
    prediction = model.predict(user_input)[0]
    probabilities = model.predict_proba(user_input)[0]

    # Menghitung probabilitas status
    proba_graduate = probabilities[0] * 100
    proba_dropout = probabilities[1] * 100

    st.markdown("#### 📢 Hasil Prediksi")
    st.write(f"{mapping[prediction]}")
    st.markdown("#### 📈 Probabilitas:")
    st.write(f"Graduate: {proba_graduate:.2f}%")
    st.write(f"Dropout: {proba_dropout:.2f}%")