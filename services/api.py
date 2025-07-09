from fastapi import FastAPI
from services.agent import react_agent

app = FastAPI()

@app.get("/query")
def query(user_id: str, q: str):
    return {"answer": react_agent(user_id, q)}
