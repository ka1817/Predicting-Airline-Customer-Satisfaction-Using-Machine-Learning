import pytest
import requests

BASE_URL = "http://localhost:4000"  # Ensure the FastAPI server is running locally before testing

@pytest.fixture
def sample_data():
    return {
        "Gender": "Male",
        "Customer_Type": "Loyal",
        "Age": 30,
        "Type_of_Travel": "Business travel",
        "Class": "Business",
        "Flight_Distance": 1500,
        "Delay_Category": "No Delay",
        "Service_Quality": "Good"
    }

def test_home():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Airlines Customer Satisfaction Prediction API!"}

def test_prediction(sample_data):
    response = requests.post(f"{BASE_URL}/predict", json=sample_data)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] in ["satisfied", "neutral or dissatisfied"]

def test_invalid_data():
    invalid_data = {
        "Gender": "Unknown",
        "Customer_Type": "Loyal",
        "Age": "Thirty",  # Invalid age type
        "Type_of_Travel": "Work",
        "Class": "VIP",
        "Flight_Distance": "Far",  # Invalid distance type
        "Delay_Category": "None",
        "Service_Quality": "Excellent"
    }
    response = requests.post(f"{BASE_URL}/predict", json=invalid_data)
    assert response.status_code == 422  # Expecting validation error from FastAPI
