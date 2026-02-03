from fastapi import FastAPI, Depends
from datetime import datetime

app = FastAPI()
# Function Level Dependency Injection

def db_connection():
    return {"Message": "DB connected sucessfully!!......"}

@app.get("/display/")
async def view(Database = Depends(db_connection)):
    return {"Message": "This is from Function Level Dependency Injection",
            "Database": Database}

# Class Level Dependency Injection
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        return ({"Name ": self.name, "Age ": self.age})

def get_user():
    user_data = User("Vijay", 24)
    return user_data

@app.get("/user_info/")
async def user_info(User = Depends(get_user)):
    return {"Message": "This is from Class Level Dependency Injection",
            "User Details": User.get_data()}

# Global Level Dependency Injection
# def verify_token(token: str="1234"):
#     if token != "1234":
#         raise Exception("Invalid Token")
#     return True

# app = FastAPI(dependencies=[Depends(verify_token)])

# @app.get("/token_sys/")
# async def view():
#     return {"Message": "This is from Global Level Dependency Injection, Token verified successfully!!..."}
#----------#


# Sub-Level Dependency Injection

def grand_parent():
    return {"Message": "This is from Grand Parent"}

def parent(gp : str = Depends(grand_parent)):
    return {"Message": "This is from Parent",
            "Grand Parent Message": gp}


@app.get("/child/")
async def child(p: str = Depends(parent)):
    return {"Message": "This is from Child",
            "Parent Message": p}

# Yeild Level Dependency Injection

def barrow_book():
    print("Book Borrowed", datetime.now())
    book = "Harry Potter"
    yield book
    print("Book Returned", datetime.now())

@app.get("/library/")
async def library(book : str = Depends(barrow_book)):
    return {"Message": "This is from Yield Level Dependency Injection",
            "Book Borrowed": book,
            "Time": datetime.now()}