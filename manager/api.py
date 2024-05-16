# fastapi_app/api.py
from fastapi import FastAPI, UploadFile, File, APIRouter
from .views import uploadtoServer
from asgiref.sync import sync_to_async
import shutil

app = FastAPI()

api = APIRouter(tags=['ServerJars'])


@app.get("/hello")
async def read_root():
    return {"message": "Hello World"}

@app.post('/upload/server')
async def uploadServer(
  file: UploadFile,
  project: str,
  version: str,
  build: int = 0,
):
  contents = await file.read()

  await sync_to_async(uploadtoServer)(file=file,filecontent=contents, project=project, version=version, build=build)
  return {"filename": file.filename}


