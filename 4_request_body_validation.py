from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

# Validation

class manf(BaseModel):
    company: str
    country: str

class kart(BaseModel):
    name: str = Field(min_length=3, max_length=10, pattern="^[a-zA-Z]")
    price: float = Field(gt=0, lt=100)
    quantity: int
    tips: Optional[int] = None
    manufacturer: manf

app = FastAPI()

@app.post("/items/")
def create_item(item: kart):
    return {"Message": "Item created successfully", "kart": item}