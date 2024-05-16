# fastapi_app/api.py
from fastapi import FastAPI, UploadFile, File, APIRouter
from .views import uploadtoServer
app = FastAPI()

api = APIRouter(tags=['ServerJars'])

@api.get('')

@app.get("/hello")
async def read_root():
    return {"message": "Hello World"}

@app.post('/upload/server')
async def uploadServer(
  file: UploadFile,
  version: str,
  project: str,

  build: int = 0,

   ):
  return {"filename": file.filename}