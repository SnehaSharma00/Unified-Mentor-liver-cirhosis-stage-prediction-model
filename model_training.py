import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib


df = pd.read_csv("data/liver_cirrhosis.csv") 

# Preprocessing 
cat_cols = ['Status', 'Drug', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema']
label_encoders = {}

for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le 

df.dropna(inplace=True) 

# Features and Target 
X = df.drop(columns=['Stage'])
y = df['Stage']

# Train/Test Split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training 
model = RandomForestClassifier(random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# Evaluation 
y_pred = model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))

# Saving the model and encoders
joblib.dump(model, 'stage_predictor.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')
