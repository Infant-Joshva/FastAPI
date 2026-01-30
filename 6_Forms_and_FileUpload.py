from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from typing import List
app = FastAPI()

# Forms

# @app.post("/feedback/")
# def feed(name : str = Form(),
#          email : str = Form(),
#          message : str = Form()):
#     return {"Status" : "Feedback submitted successfully", 
#             "name": name,
#             "message": message
#             }   

#----------#

# File Upload

@app.post("/file-upload/")
async def file_upload(files : List[UploadFile] = File(...)):
    
    result = []
    for file in files:
        content = await file.read()
        try:
            text_preview = content[:100]
        except:
            text_preview = "Cannot preview the file"

        result.append({
            "filename": file.filename,
            "filetype": file.content_type,
            "len of the content in letters": len(content),
            "preview": text_preview
        })
    return result
    













