from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
from PIL import Image
import os

app = FastAPI()

def convert_to_png(file_path):
    """Konwertuje plik HEIC/HEIF/JPG na PNG i zwraca nową ścieżkę"""
    if file_path.lower().endswith((".heic", ".heif", ".jpg", ".jpeg")):
        img = Image.open(file_path)
        png_path = file_path.rsplit(".", 1)[0] + ".png"
        img.save(png_path, format="PNG")
        return png_path
    return file_path

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    
    # Zapisz przesłany plik
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Konwertuj na PNG jeśli potrzebne
    processed_path = convert_to_png(file_path)

    # Wczytaj obraz do OpenCV
    image = cv2.imread(processed_path)

    if image is None:
        return {"diagnosis": "Could not process the image."}

    # **Przykładowa logika wykrywania pęknięć (można rozwinąć)**
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    if np.sum(edges) > 100000:  # Przykładowy próg detekcji pęknięć
        return {"diagnosis": "Detected crack in concrete, recommended injection sealing."}
    
    return {"diagnosis": "No significant cracks detected."}

from PIL import Image
import os

def convert_to_png(file_path):
    """Konwertuje plik HEIC/HEIF/JPG na PNG i zwraca nową ścieżkę"""
    if file_path.lower().endswith((".heic", ".heif", ".jpg", ".jpeg")):
        img = Image.open(file_path)
        png_path = file_path.rsplit(".", 1)[0] + ".png"
        img.save(png_path, format="PNG")
        return png_path
    return file_path
‹