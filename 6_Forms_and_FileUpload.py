from fastapi import FastAPI, Form, File, UploadFile, HTTPException

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
async def file_upload(File : UploadFile = File(...)):
    content = await File.read()

    try:
        text_preview = content[:100]
    except e:
        text_preview = "Cannot preview the file"

    return {
        "filename": File.filename,
        "filetype": File.content_type,
        "len of the content in letters": len(content),
        "preview": text_preview
    }

    













