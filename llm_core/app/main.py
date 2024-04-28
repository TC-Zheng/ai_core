from fastapi import FastAPI
from llm_core.app.llm_router import router as llm_router
import uvicorn

app = FastAPI()
app.include_router(llm_router)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
