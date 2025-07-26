🚦 Traffic Flow Predictor using Machine Learning
A Streamlit app that predicts traffic conditions based on user inputs such as vehicle counts, day, time, and date. It uses a Random Forest ML model and rule-based logic to display both encoded and interpretable traffic outputs.

📈 Features
Predicts traffic levels using a trained Random Forest model.
Displays:

🔢 Encoded prediction (numeric)

🗋 Label-based prediction (interpretable)

Rule-based categorization:

≤ 10 vehicles: Low
11–50: Moderate
51–100: Normal
100: High

Built with an intuitive Streamlit UI.

🛠️ Tech Stack

Tool

Python-->Programming language

Streamlit-->Web app interface

scikit-learn-->ML model training

joblib-->Model persistence

NumPy-->Data manipulation


📁 Project Structure

traffic-flow-predictor/

├── app.py                    # Main Streamlit app

├── traffic_rf_model.pkl      # Saved ML model & label encoder

├── README.md                 # Project overview


