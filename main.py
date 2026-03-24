from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load tools data
with open("tools.json", "r") as file:
    tools_data = json.load(file)

@app.get("/")
def home():
    return {"message": "ToolStack API is running"}

@app.get("/recommend")
def recommend(query: str):
    query = query.lower()
    results = []

    for category in tools_data:
        for tool in tools_data[category]:
            for tag in tool["tags"]:
                if tag in query:
                    results.append(tool)
                    break

    return {"results": results}