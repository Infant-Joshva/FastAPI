from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

# Query parameters validation

emp = [
    {"id": 1, "name": "vijay"},
    {"id": 2, "name": "ajith"},
    {"id": 3, "name": "karthik"},
]
app = FastAPI()

# Path parameters validation
@app.get("/display/{id}")
def ViewForQuery(id: int):  
    for e in emp:
        if e["id"] == id:
            return e

# Query parameters validation
# @app.get("/display")
# def ViewForQuery(id: int = Query(ge=1, le=3)):
#     for e in emp:
#         if e["id"] == id:
#             return e
        
@app.get("/display")
def ViewForQuery(id : int = Query(ge=1, le=3), name: str = Query(min_length=3, max_length=10, regex="^[a-zA-Z]")):
    for e in emp:
        if e[id] == id and e["name"].lower() == name.lower():
            return e