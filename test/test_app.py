import requests

API_URL = "http://127.0.0.1:4000/predict"

def test_home():
    response = requests.get("http://127.0.0.1:4000/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Airlines Customer Satisfaction Prediction API!"}

def test_prediction():
    test_data = {
        "Gender": "Male",
        "Customer_Type": "Loyal",
        "Age": 30,
        "Type_of_Travel": "Business travel",
        "Class": "Business",
        "Flight_Distance": 1000,
        "Delay_Category": "No Delay",
        "Service_Quality": "Excellent"
    }
    response = requests.post(API_URL, json=test_data)
    assert response.status_code == 200
    assert "prediction" in response.json()
