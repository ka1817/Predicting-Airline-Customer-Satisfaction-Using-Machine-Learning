import joblib
import pandas as pd
import mlflow.sklearn

model_path = "models/Rfc_model.pkl"  
model = joblib.load(model_path)

feature_names = [
    "Gender", "Customer Type", "Age", "Type of Travel", "Class", 
    "Flight Distance", "Delay_Category", "Service_Quality"
]

new_data = pd.DataFrame([[
    "Male", "Loyal Customer", 25, "Personal Travel", "Eco Plus", 
    700, "No Delay", "Average"
]], columns=feature_names)

prediction = model.predict(new_data)

print(f"Predicted Satisfaction: {prediction[0]}")
