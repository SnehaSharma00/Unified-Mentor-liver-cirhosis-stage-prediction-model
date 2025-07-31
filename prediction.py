import pandas as pd
import joblib

model = joblib.load('stage_predictor.pkl')
label_encoders = joblib.load('label_encoders.pkl')

# Sample Input (change values to test different patients) 
sample = {
    'N_Days': 2500,
    'Status': 'C',
    'Drug': 'Placebo',
    'Age': 18000,
    'Sex': 'F',
    'Ascites': 'N',
    'Hepatomegaly': 'Y',
    'Spiders': 'N',
    'Edema': 'N',
    'Bilirubin': 1.2,
    'Cholesterol': 250,
    'Albumin': 3.5,
    'Copper': 80,
    'Alk_Phos': 1000,
    'SGOT': 110,
    'Tryglicerides': 150,
    'Platelets': 300,
    'Prothrombin': 10.0
}

input_df = pd.DataFrame([sample])

# Encode categorical values
for col, le in label_encoders.items():
    input_df[col] = le.transform(input_df[col].astype(str))

# Predict 
prediction = model.predict(input_df)[0]
print(f"Predicted Liver Cirrhosis Stage: {prediction}")
