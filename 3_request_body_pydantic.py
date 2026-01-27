from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Pydantic

class kart(BaseModel):
    name: str
    price: float
    quantity: int
    tips: Optional[int] = None

app = FastAPI()

@app.post("/items/")
def create_item(item: kart):
    return {"Message": "Item created successfully", "kart": item}