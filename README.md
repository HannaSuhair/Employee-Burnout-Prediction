# Employee-Burnout-Prediction
Streamlit ML app that predicts employee burnout risk
## About the project
Burnout affects productivity and wellbeing. This project uses machine learning to flag burnout risk from details like work hours, sleep, commute time and work-life balance.

## Tech stack
Python • Pandas • NumPy • Scikit-learn • Streamlit

## Model
- Compared several classification algorithms, including Logistic Regression, Random Forest and Decision Tree
- Final model: Logistic Regression (tuned with regularization)
- Features scaled with a scaler
- Accuracy: 68%
- Uses 11 input features

## Files
- employee_burnout.py: Streamlit app
- project.ipynb: data analysis and model building
- mental_health_workplace_survey.csv: dataset
- burnout_model1.pkl and scaler_final.pkl: saved model and scaler
- requirements.txt: dependencies

## Run it locally
```
pip install -r requirements.txt
streamlit run employee_burnout.py
```

## Author
Hanna Haneef
