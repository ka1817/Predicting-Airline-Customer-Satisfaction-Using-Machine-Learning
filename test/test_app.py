import pytest
import requests
import time

BASE_URL = "http://localhost:4000"  

def wait_for_api(timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(f"{BASE_URL}/")
            if response.status_code == 200:
                return True
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(2)  # Wait and retry
    raise RuntimeError("FastAPI server not available.")

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
    wait_for_api()
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
        "Age": "Thirty", 
        "Type_of_Travel": "Work",
        "Class": "VIP",
        "Flight_Distance": "Far", 
        "Delay_Category": "None",
        "Service_Quality": "Excellent"
    }
    response = requests.post(f"{BASE_URL}/predict", json=invalid_data)
    assert response.status_code == 422 
