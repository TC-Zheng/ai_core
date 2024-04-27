

# class DownloadLLMService:
#     def __init__(self, model_id: str):
#         self.model_id = model_id

#     def download_model(self):
#         # Define the directory where you want to store the models
#         model_directory = os.path.join("models", self.model_id)
#         os.makedirs(model_directory, exist_ok=True)

#         # Download the model from Hugging Face
#         model = AutoModel.from_pretrained(self.model_id)

#         # Save the model locally
#         model.save_pretrained(model_directory)

#         return {"message": f"Model {self.model_id} downloaded and saved successfully."}