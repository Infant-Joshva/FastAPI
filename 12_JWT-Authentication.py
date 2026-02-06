from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta
from jose import jwt, JWTError

# Fisrt we are going to create a endpoint for login
# Then we are going to create a endpoint for home (secret data)
# Next JWT Token creation
# Verification of created Token

# Structure of JWT Token:
# 1. Header
# 2. Payload
# 3. Signature

# configuration setup:
# Type = JWT
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1
SECRET_KEY = "MySecretKey"


app = FastAPI()

def create_token(uname: str):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    #Payload
    payload = {
        "username": uname,
        "exp": expire
    }
    #Signature
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # print(payload)
        return payload["username"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or Expired token") 


@app.post("/login")
def login(uname: str, password: str):
    if uname == "admin" and password == "1234":
        token = create_token(uname)
        return {"access token": token}
    return HTTPException(status_code=401, detail="Invalid or Expired token")

@app.get("/secure_data")
def sec_data(token: str):
    uname = verify_token(token)
    return {"Message": f"Hello {uname} this is secure endpoint"}



