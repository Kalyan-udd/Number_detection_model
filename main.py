from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import UploadFile, File
import joblib
import uvicorn
from src.Number_recognition_model.logger import logger
import numpy as np
from PIL import Image
import io


app = FastAPI()


model = joblib.load("artifacts/number_recogniser.joblib")


@app.get("/")
async def home_page():
    return FileResponse("templates/home.html")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("L").resize((28,28))
    image_array = np.array(image)
    x_predict = image_array/255.0
    x_predict = np.expand_dims(x_predict, axis=0)
    y_predicted = model.predict(x_predict)

    result = int(np.argmax(y_predicted))
    confidence = float(np.max(y_predicted))

    return {
        "predicted_digit": result,
        "confidence": confidence
    }


