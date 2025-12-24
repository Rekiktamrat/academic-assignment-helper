from fastapi import FastAPI, UploadFile, Depends
from auth import create_token, get_current_student
import shutil, requests

app = FastAPI()

@app.post("/auth/register")
def register():
    return {"msg": "Registered (mocked)"}

@app.post("/auth/login")
def login():
    token = create_token({"role": "student"})
    return {"access_token": token}

@app.post("/upload")
def upload(file: UploadFile, user=Depends(get_current_student)):
    path = f"uploads/{file.filename}"
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    requests.post("http://localhost:5678/webhook/assignment", json={
        "file_path": path
    })

    return {"job_id": file.filename}

@app.get("/analysis/{id}")
def get_analysis(id: int, user=Depends(get_current_student)):
    return {"status": "completed", "score": 0.23}
