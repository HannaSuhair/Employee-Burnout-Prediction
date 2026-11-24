
import streamlit as st
import numpy as np
import pickle


# Page config
st.set_page_config(
    page_title="Employee Burnout Prediction",
    page_icon="🏢",
    layout="wide"
)

# CSS Styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f4f8;
    }
    .stApp {
        background: linear-gradient(135deg, #0a1628 0%, #1a3a5c 100%);
    }
    .title-box {
        background: linear-gradient(90deg, #1565C0, #1E88E5);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(21,101,192,0.4);
    }
    .title-box h1 {
        color: white;
        font-size: 2.2em;
        margin: 0;
    }
    .title-box p {
        color: #90CAF9;
        margin: 5px 0 0 0;
    }
    .section-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .section-title {
        color: #64B5F6;
        font-size: 1.1em;
        font-weight: bold;
        margin-bottom: 15px;
        border-bottom: 2px solid #1565C0;
        padding-bottom: 8px;
    }
    .stSlider label, .stSelectbox label {
        color: #B0BEC5 !important;
    }
    .predict-btn button {
        background: linear-gradient(90deg, #1565C0, #1E88E5) !important;
        color: white !important;
        font-size: 1.2em !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        padding: 15px !important;
        width: 100% !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(21,101,192,0.5) !important;
    }
    .result-high {
        background: linear-gradient(90deg, #b71c1c, #e53935);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 1.4em;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(183,28,28,0.4);
    }
    .result-low {
        background: linear-gradient(90deg, #1b5e20, #43a047);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 1.4em;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(27,94,32,0.4);
    }
    </style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open('burnout_model1.pkl', 'rb'))
scaler = pickle.load(open('scaler_final.pkl', 'rb'))

# Header
st.markdown("""
    <div class="title-box">
        <h1>🏢 Employee Burnout Prediction System</h1>
        <p>AI-powered burnout risk assessment for HR professionals</p>
    </div>
""", unsafe_allow_html=True)

# Layout - 3 columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="section-title">👤 Personal Info</div>', unsafe_allow_html=True)
    age = st.slider("Age", 20, 60, 30)
    gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Male" if x==0 else "Female")
    years = st.slider("Years At Company", 0, 20, 5)
    remote = st.selectbox("Remote Work", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    team = st.slider("Team Size", 2, 20, 8)

with col2:
    st.markdown('<div class="section-title">💼 Work Factors</div>', unsafe_allow_html=True)
    work_hours = st.slider("Work Hours Per Week", 20, 80, 40)
    stress = st.slider("Stress Level (1-10)", 1, 10, 5)
    burnout_level = st.slider("Burnout Level (1-10)", 1.0, 10.0, 5.0)
    satisfaction = st.slider("Job Satisfaction (1-10)", 1, 10, 5)
    productivity = st.slider("Productivity Score (1-10)", 1, 10, 5)
    salary = st.slider("Salary Range (1-5)", 1, 5, 3)

with col3:
    st.markdown('<div class="section-title">🏥 Health & Wellness</div>', unsafe_allow_html=True)
    sleep = st.slider("Sleep Hours", 4, 10, 7)
    physical = st.slider("Physical Activity Hrs", 0, 10, 3)
    commute = st.slider("Commute Time (mins)", 10, 120, 30)
    mental_days = st.slider("Mental Health Days Off", 0, 30, 5)
    worklife = st.slider("Work Life Balance (1-10)", 1, 10, 5)
    career = st.slider("Career Growth Score (1-10)", 1, 10, 5)
    mental_support = st.selectbox("Mental Health Support", [0,1], format_func=lambda x: "No" if x==0 else "Yes")
    therapy = st.selectbox("Therapy Access", [0,1], format_func=lambda x: "No" if x==0 else "Yes")

# Predict Button
st.markdown("<br>", unsafe_allow_html=True)
col_btn = st.columns([1,2,1])
with col_btn[1]:
    predict = st.button("🔍 Predict Burnout Risk")

# Prediction
if predict:
    input_data = np.array([[age, gender, years, work_hours,
                            remote, satisfaction, stress,
                            sleep, commute, worklife, career]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0]

    st.markdown("<br>", unsafe_allow_html=True)
    if prediction == 1:
        st.markdown("""
            <div class="result-high">
                ⚠️ HIGH BURNOUT RISK DETECTED!<br>
                <span style="font-size:0.7em">Immediate intervention recommended</span>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="result-low">
                  LOW BURNOUT RISK<br>
                <span style="font-size:0.7em">Employee appears to be in good shape!</span>
            </div>
        """, unsafe_allow_html=True)

    # Probability bar
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("**Risk Probability:**")
    st.progress(float(probability[1]))
    st.caption(f"Burnout probability: {probability[1]*100:.1f}%")