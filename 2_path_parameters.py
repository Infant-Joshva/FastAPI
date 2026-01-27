from fastapi import FastAPI, HTTPException

emp = [
    {"id": 1, "name": "vijay"},
    {"id": 2, "name": "ajith"},
    {"id": 3, "name": "karthik"},
]
app = FastAPI()

# @app.get("/items/{item_id}")
# def for_path_parameters(item_id: int):
#     return {"item_id": item_id}

# @app.get("/items/{item_id}") 
# def for_path_parameters(item_id: int): # Search with ID
#     for i in emp:
#         if i["id"] == item_id:
#             return i

# @app.get("/items/{item_name}") 
# def for_path_parameters(item_name: str): # Search with name
#     for i in emp:
#         if i["name"] == item_name:
#             return i

#-------#

# Query parameters
@app.get("/items/")
def for_queryparameters(q_id: int): # Search with name
    for i in emp:
        if i["id"] == q_id:
            return i