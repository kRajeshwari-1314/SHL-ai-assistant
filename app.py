from fastapi import FastAPI
from pydantic import BaseModel

from utils.retriever import retrieve_assessments
from utils.llm_handler import generate_response

app = FastAPI()


# Request schema
class ChatRequest(BaseModel):
    query: str


# Health endpoint
@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


# Chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):

    # Ask clarification questions for vague queries
    vague_words = [
        "developer",
        "engineer",
        "assessment",
        "test",
        "job"
    ]

    if any(word in request.query.lower() for word in vague_words):

        if len(request.query.split()) < 4:

            return {
                "clarification_needed": True,
                "message": (
                    "Please provide more details such as "
                    "skills, experience level, programming language, "
                    "or job role."
                )
            }

    # Retrieve relevant assessments
    retrieved_results = retrieve_assessments(request.query)

    # Generate AI response
    response = generate_response(
        request.query,
        retrieved_results
    )

    return {
        "query": request.query,
        "response": response,
        "recommendations": retrieved_results
    }