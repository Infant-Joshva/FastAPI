from fastapi import FastAPI, File, UploadFile
import pandas as pd
from PyPDF2 import PdfReader
import io


app = FastAPI()

# File Upload

@app.post("/file-upload/")
async def file_upload(file : UploadFile = File(...)):
    content = await file.read()
    name = file.filename.lower()

    if name.endswith((".xls",".xlsx")):
        df=pd.read_excel(io.BytesIO(content))
        return {"Type" : "Excel", "Preview" : df.head(4).to_dict()}

    elif name.endswith(".pdf"):
        reader = 













