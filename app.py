from fastapi import FastAPI
from pydantic import BaseModel
from src.serenhive.risk import assess_content

app = FastAPI(title="SerenHive Agent", version="0.1.0")

class ContentRequest(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/content/assess")
def content_assess(request: ContentRequest):
    assessment = assess_content(request.text)
    return assessment.model_dump()
