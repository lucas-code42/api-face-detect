import base64

import cv2
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel


class Detector(BaseModel):
    base64_image: str


app = FastAPI()


@app.post("/detect")
async def detect_faces(item: Detector,
                       description="""Rota implementa algoritimo haarcascade_frontalface forncecido pela OpenCv. 
                       A rota devolve um json informando quantos rostos foram detectados"""):
    img_content = base64.b64decode(item.base64_image)
    img_array = np.frombuffer(img_content, dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30))

    response = {"facesFound": len(faces)}
    return response
