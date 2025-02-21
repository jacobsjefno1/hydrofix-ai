from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Hydrofix AI is running!"}

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # 🚀 Prosta analiza zdjęcia (AI będzie później)
    if img is not None:
        result = "Detected crack in concrete, recommended injection sealing."
    else:
        result = "Could not process the image."

    return {"diagnosis": result}
