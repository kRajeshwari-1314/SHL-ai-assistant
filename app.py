from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request schema
class ChatRequest(BaseModel):
    query: str


# Health endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Temporary safe chat endpoint (NO imports, NO crash)
@app.post("/chat")
def chat(request: ChatRequest):

    return {
        "query": request.query,
        "response": "API is working (debug mode)",
        "recommendations": []
    }