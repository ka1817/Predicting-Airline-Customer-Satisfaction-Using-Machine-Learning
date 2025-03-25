import unittest
import requests
import time
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

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
        time.sleep(2)  
    raise RuntimeError("FastAPI server not available.")

class TestFastAPIApp(unittest.TestCase):
    
    def test_home(self):
        wait_for_api()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to the Airlines Customer Satisfaction Prediction API!"})

    def test_predict_valid_data(self):
        sample_data = {
            "Gender": "Male",
            "Customer_Type": "Loyal",
            "Age": 30,
            "Type_of_Travel": "Business travel",
            "Class": "Business",
            "Flight_Distance": 1500,
            "Delay_Category": "No Delay",
            "Service_Quality": "Good"
        }
        response = client.post("/predict", json=sample_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.json())
        self.assertIn(response.json()["prediction"], ["satisfied", "neutral or dissatisfied"])

    def test_predict_invalid_data(self):
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
        response = client.post("/predict", json=invalid_data)
        self.assertEqual(response.status_code, 422)  

if __name__ == "__main__":
    unittest.main()