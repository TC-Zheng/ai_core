import os
import asyncio
from transformers import AutoModel, AutoTokenizer

class AsyncModelRepository:
    def __init__(self, directory):
        self.directory = directory
        os.makedirs(directory, exist_ok=True)

    async def save_model_and_tokenizer(self, model, tokenizer, model_name):
        model_path = os.path.join(self.directory, model_name)
        tokenizer_path = os.path.join(self.directory, model_name + '_tokenizer')
        temp_model_path = model_path + "_tmp"
        temp_tokenizer_path = tokenizer_path + "_tmp"

        try:
            # Save to a temporary directory
            await asyncio.gather(
                asyncio.to_thread(model.save_pretrained, temp_model_path),
                asyncio.to_thread(tokenizer.save_pretrained, temp_tokenizer_path)
            )

            # If save succeeds, rename the directory
            os.rename(temp_model_path, model_path)
            os.rename(temp_tokenizer_path, tokenizer_path)
        except Exception as e:
            # Handle exceptions, possibly logging them, and cleaning up the temp directory
            print(f"Failed to save model and tokenizer {model_name}: {e}")
            try:
                if os.path.exists(temp_model_path):
                    os.rmdir(temp_model_path)
                if os.path.exists(temp_tokenizer_path):
                    os.rmdir(temp_tokenizer_path)
            except Exception as e:
                print(f"Failed to clean up: {e}")

    async def load_model_and_tokenizer(self, model_name):
        model_path = os.path.join(self.directory, model_name)
        tokenizer_path = os.path.join(self.directory, model_name + '_tokenizer')

        try:
            # Load model and tokenizer from directory
            model, tokenizer = await asyncio.gather(
                asyncio.to_thread(AutoModel.from_pretrained, model_path),
                asyncio.to_thread(AutoTokenizer.from_pretrained, tokenizer_path)
            )
            return model, tokenizer
        except Exception as e:
            print(f"Failed to load model and tokenizer {model_name}: {e}")
            return None, None