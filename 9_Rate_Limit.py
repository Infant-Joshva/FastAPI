from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

req_counter = {}
max_req = 5

@app.get("/data/")
def get_data(req : Request):
    client_ip = req.client.host
    req_counter[client_ip] = req_counter.get(client_ip, 0) + 1

    print(req_counter)

    if req_counter[client_ip] > max_req:
        raise HTTPException(status_code=429, detail="Your request limit has been exceeded. Please try again later.....")

    return {"message":f"Request {req_counter[client_ip]} sent successfully",
            "Balance requests left" : str(max_req - req_counter[client_ip])}
