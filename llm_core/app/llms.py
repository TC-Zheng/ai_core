from fastapi import APIRouter, HTTPException
from transformers import AutoModel
import os

router = APIRouter()
test = "test"
@router.post("/download_model/")
async def download_model(model_id: str):
    try:
        # Define the directory where you want to store the models
        model_directory = os.path.join("models", model_id)
        os.makedirs(model_directory, exist_ok=True)

        # Download the model from Hugging Face
        model = AutoModel.from_pretrained(model_id)

        # Save the model locally
        model.save_pretrained(model_directory)

        return {"message": f"Model {model_id} downloaded and saved successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))