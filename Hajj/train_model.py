import pandas as pd
import numpy as np
import os
import joblib

# TensorFlow environment settings to resolve DLL issues and reduce warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.preprocessing import StandardScaler, LabelEncoder

# 1. Directory Setup
if not os.path.exists('ai_models'):
    os.makedirs('ai_models')

# 2. Load Data
file_name = 'Hajj_Final_Scientific_Data_.xlsx'
df = pd.read_excel(file_name)

# Clean column names
df.columns = df.columns.str.strip()

# 3. Categorical Data Processing
# Converting 'Age Group' into numerical values
le = LabelEncoder()
df['Age Group_Encoded'] = le.fit_transform(df['Age Group'])
joblib.dump(le, 'ai_models/label_encoder.pkl')

# 4. Define Features and Targets
features = [
    'Age Group_Encoded', 'Number of pilgrims', 'Temperature_C',
    'Humidity_Pct', 'Wind_Speed_kmh', 'Hospitals',
    'Health_Centers', 'Bed_Capacity', 'Staff_Count', 'Ambulances',
    'Expected_Chronic_Count'
]
targets = ['Expected_Heatstroke_Count']

X = df[features]
y = df[targets]

# 5. Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
joblib.dump(scaler, 'ai_models/scaler.pkl')

# 6. Building the Deep Neural Network (DNN) Architecture
model = Sequential([
    Dense(128, activation='relu', input_shape=(len(features),)),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='linear')
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# 7. Training Phase
print("⏳ Training the Smart Health System...")
model.fit(X_scaled, y, epochs=100, batch_size=8, verbose=1)

# 8. Saving the Final Model
model.save('ai_models/hajj_health_model.h5')
print("\n" + "="*30)
print("✅ DNN model generated and saved successfully!")
print("📁 Path: ai_models/hajj_health_model.h5")
print("="*30)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Weather Prediction System Running Successfully!"
