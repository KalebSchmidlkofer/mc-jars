# fastapi_app/api.py
from fastapi import FastAPI, UploadFile, File, APIRouter
from .views import uploadtoModded, uploadtoServer, uploadtoOther, uploadtoProxy, uploadtoVanilla, uploadtoBedrock
from asgiref.sync import sync_to_async
import shutil

app = FastAPI()

api = APIRouter(tags=['Upload'])



@app.post('/upload/servers')
async def uploadServer(
  file: UploadFile,
  project: str,
  version: str,
  build: int = 0,
):
  contents = await file.read()

  await sync_to_async(uploadtoServer)(file=file,filecontent=contents, project=project, version=version, build=build)
  return {"filename": file.filename}

@app.post('/upload/modded')
async def uploadModded(
  file: UploadFile,
  project: str,
  version: str,
  build: int = 0,
):
  contents = await file.read()

  await sync_to_async(uploadtoModded)(file=file,filecontent=contents, project=project, version=version, build=build)
  return {"filename": file.filename}

@app.post('/upload/vanilla')
async def uploadVanilla(
  file: UploadFile,
  project: str,
  version: str,
  build: int = 0,
):
  contents = await file.read()

  await sync_to_async(uploadtoVanilla)(file=file,filecontent=contents, project=project, version=version, build=build)
  return {"filename": file.filename}

@app.post('/upload/bedrock')
async def uploadBedrock(
  file: UploadFile,
  project: str,
  version: str,
  build: int = 0,
):
  contents = await file.read()

  await sync_to_async(uploadtoBedrock)(file=file,filecontent=contents, project=project, version=version, build=build)
  return {"filename": file.filename}

@app.post('/upload/proxy')
async def uploadProxy(
  file: UploadFile,
  project: str,
  version: str,
  build: int = 0,
):
  contents = await file.read()

  await sync_to_async(uploadtoProxy)(file=file,filecontent=contents, project=project, version=version, build=build)
  return {"filename": file.filename}

@app.post('/upload/misc')
async def uploadMisc(
  file: UploadFile,
  project: str,
  version: str,
  build: int = 0,
):
  contents = await file.read()

  await sync_to_async(uploadtoOther)(file=file,filecontent=contents, project=project, version=version, build=build)
  return {"filename": file.filename}