from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pipeline import run_research_pipeline

app = FastAPI()

# CORS so the UI can talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResearchRequest(BaseModel):
    topic: str

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.post("/research")
def research_topic(request: ResearchRequest):
    result = run_research_pipeline(request.topic)
    return {
        "status": "success",
        "topic": request.topic,
        "data": result
    }
