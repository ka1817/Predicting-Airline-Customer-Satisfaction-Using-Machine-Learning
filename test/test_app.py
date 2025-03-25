import joblib
import pandas as pd
import pytest

# Load Model for Direct Testing
MODEL_PATH = "models/gb_model.pkl"
model = joblib.load(MODEL_PATH)

# Define feature names
feature_names = [
    "Gender", "Customer Type", "Age", "Type of Travel", "Class", 
    "Flight Distance", "Delay_Category", "Service_Quality"
]

@pytest.fixture(scope="module")
def loaded_model():
    """Load the model once for all tests"""
    return model

def test_model_prediction(loaded_model):
    """Test direct model prediction with a sample input"""
    new_data = pd.DataFrame([[
        "Male", "Loyal Customer", 25, "Personal Travel", "Eco Plus", 
        700, "No Delay", "Average"
    ]], columns=feature_names)

    prediction = loaded_model.predict(new_data)
    assert prediction in [0, 1]  # Assuming 0: Not Satisfied, 1: Satisfied
    print(f"Predicted Satisfaction: {prediction[0]}")
