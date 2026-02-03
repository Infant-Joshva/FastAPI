from fastapi import FastAPI, HTTPException, Cookie, Response
from datetime import datetime, timedelta
from typing import Optional
import uuid

app = FastAPI()

user_name = "admin"
user_password = "1234"
session = {}
timer=10

@app.post("/login")
def login(uname: str, pas: str, res: Response):
    if uname == user_name and pas == user_password:
        sid = str(uuid.uuid4())
        current_time = datetime.now()
        expiry_time = current_time + timedelta(seconds=timer)
        # print("Current Time:", current_time, "expiry_time:", expiry_time)
        session[sid] = {"ID" : sid,"username": uname, "expiry_time": expiry_time}
        res.set_cookie(key="session_id", value=sid, httponly=True, max_age=timer)
        return {"message": "Login successfullly!...."}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/home")
def home(session_id: Optional[str] = Cookie(None)):
    if session_id is None or session_id not in session:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    if datetime.now() > session[session_id]["expiry_time"]:
        del session[session_id]
        raise HTTPException(status_code=401, detail="Session expired")

    return {"message": f"Welcome {session[session_id]['username']} your ID is {session_id} and the expiry time is {session[session_id]['expiry_time']}" }
