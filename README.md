# AI-Powered Weather Prediction System for Pilgrim Health in Makkah

## Overview
This project is an AI-powered weather prediction and health risk analysis system developed to enhance pilgrim safety during Hajj seasons in Makkah.

The system combines weather analytics, healthcare data, and Deep Neural Networks (DNN) to predict potential health risks such as heat exhaustion and heatstroke. It also integrates the Wet-Bulb Globe Temperature (WBGT) index to improve heat stress evaluation and provide preventive recommendations in real time.

## Features
- AI-based weather prediction system
- Pilgrim health risk classification
- WBGT heat index integration
- Deep learning model using TensorFlow/Keras
- Real-time preventive recommendations
- Data visualization and performance evaluation
- Dashboard interfaces for monitoring and analysis

## Technologies Used
- Python
- TensorFlow / Keras
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Project Structure

```bash
Hajj/
│── app.py
│── model_handler.py
│── evaluate.py
│── requirements.txt
│── ai_models/
│   ├── hajj_health_model.h5
│   ├── scaler.pkl
│   └── label_encoder.pkl
│── data/
│   ├── Hajj_Final_Scientific_Data.xlsx
│   ├── Hajj_Clinical_Data_1444.xlsx
│   └── Hajj_Data_With_Resources.csv
│── confusion_matrix_result.png
│── final_performance_matrix.png
└── README.md
