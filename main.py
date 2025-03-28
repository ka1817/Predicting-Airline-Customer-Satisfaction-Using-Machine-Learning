from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn

app = FastAPI(title="Airlines Customer Satisfaction Prediction API")

model_path = "gb_model.pkl"
model = joblib.load(model_path)

class CustomerFeatures(BaseModel):
    Gender: str
    Customer_Type: str
    Age: int
    Type_of_Travel: str
    Class: str
    Flight_Distance: int
    Delay_Category: str
    Service_Quality: str
@app.get("/")
def home():
    return {"message": "Welcome to the Airlines Customer Satisfaction Prediction API!"}

@app.post("/predict")
def predict_satisfaction(features: CustomerFeatures):
    data = pd.DataFrame([features.model_dump()])
    
    data.rename(columns={
        "Type_of_Travel": "Type of Travel",
        "Flight_Distance": "Flight Distance",
        "Customer_Type": "Customer Type"
    }, inplace=True)
    
    prediction = model.predict(data)
    
    return {"prediction": str(prediction[0])} 

if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0',port=4000)
