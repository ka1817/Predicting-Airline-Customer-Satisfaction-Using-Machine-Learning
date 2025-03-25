import joblib
import pandas as pd
import pytest

MODEL_PATH = "models/gb_model.pkl"
model = joblib.load(MODEL_PATH)

feature_names = [
    "Gender", "Customer Type", "Age", "Type of Travel", "Class", 
    "Flight Distance", "Delay_Category", "Service_Quality"
]

EXPECTED_LABELS = {"neutral or dissatisfied", "satisfied"}

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

    prediction = loaded_model.predict(new_data)[0]  # Extract single prediction

    assert prediction in EXPECTED_LABELS, f"Unexpected prediction: {prediction}"
    print(f"Predicted Satisfaction: {prediction}")
