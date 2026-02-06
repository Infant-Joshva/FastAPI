import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

conn=sqlite3.connect("test.db", check_same_thread=False)
cursor=conn.cursor()
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL,
#         password TEXT NOT NULL
#     )
# ''')
# conn.commit()

class user_details(BaseModel):
    username: str
    password: str

# Insert operation
@app.post("/user/register/")
def register_user(user: user_details):
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user.username, user.password))
        conn.commit()
        return {"message": "User registered successfully"}
    except:
        raise HTTPException(status_code=400, detail="Unable to register user")

# Read operation
@app.get("/read/")
def read_data():
    try:
        cursor.execute("SELECT * FROM users")
        row=cursor.fetchall()
        return [{"id":row[0], "username":row[1], "password":row[2]} for row in row]
    except:
        raise HTTPException(status_code=400, detail="Unable to read data")

@app.get("/read_one/{id}")
def readone(id: int):
    try:
        cursor.execute("SELECT * FROM users WHERE id=?", (id,))
        row=cursor.fetchone()
        return {"id":row[0], "username":row[1], "password":row[2]}
    except:
        raise HTTPException(status_code=404, detail="User not found")
    
# Update Operation

@app.put("/update/{id}")
def update_user(id: int, user: user_details):
    try:
        cursor.execute("UPDATE users SET username=?, password=? WHERE id=?", (user.username, user.password, id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User updated successfully"}
    except:
        raise HTTPException(status_code=404, detail="Unable to update")
    
# Delete Operation
@app.delete("/delete/{id}")
def delete_user(id: int):
    try:
        cursor.execute("DELETE FROM users WHERE id=?", (id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}
    except:
        raise HTTPException(status_code=404, detail="Unable to delete")