# fastapi_app/api.py
from typing import Annotated
from fastapi import FastAPI, UploadFile, File, APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from .views import uploadtoModded, uploadtoServer, uploadtoOther, uploadtoProxy, uploadtoVanilla, uploadtoBedrock
from asgiref.sync import sync_to_async
from pydantic import BaseModel

from django.contrib.auth.models import User
app = FastAPI()


def get_current_user() -> User:
    user = django.contrib.auth.get_user()
    if not user.is_authenticated:
        raise HTTPException(status_code=401, detail="User not authenticated")
    return user

class UserProfile(BaseModel):
    username: str
    email: str


@app.get('/user', response_model=UserProfile)
async def get_user_profile(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username, "email": current_user.email}

@app.post('/upload/servers')
async def uploadServer(
  # current_user: User = Depends(get_current_user),
  file: UploadFile = '',
  project: str = '',
  version: str = '',
  build: int = 0,
):
  contents = await file.read()

  await sync_to_async(uploadtoServer)(file=file,filecontent=contents, project=project, version=version, build=build)
  return {"filename": file.filename}

@app.post('/upload/modded')
async def uploadModded(
  # current_user: User = Depends(get_current_user),
  file: UploadFile = '',
  project: str = '',
  version: str = '',
  build: int = 0,
):
  contents = await file.read()

  await sync_to_async(uploadtoModded)(file=file,filecontent=contents, project=project, version=version, build=build)
  return {"filename": file.filename}

@app.post('/upload/vanilla')
async def uploadVanilla(
  # current_user: User = Depends(get_current_user),
  file: UploadFile = '',
  project: str = '',
  version: str = '',
  build: int = 0,
):
  contents = await file.read()

  await sync_to_async(uploadtoVanilla)(file=file,filecontent=contents, project=project, version=version, build=build)
  return {"filename": file.filename}

@app.post('/upload/bedrock')
async def uploadBedrock(
  # current_user: User = Depends(get_current_user),
  file: UploadFile = '',
  project: str = '',
  version: str = '',
  build: int = 0,
):
  contents = await file.read()

  await sync_to_async(uploadtoBedrock)(file=file,filecontent=contents, project=project, version=version, build=build)
  return {"filename": file.filename}

@app.post('/upload/proxies')
async def uploadProxy(
  # current_user: User = Depends(get_current_user),
  file: UploadFile = '',
  project: str = '',
  version: str = '',
  build: int = 0,
):
  contents = await file.read()

  await sync_to_async(uploadtoProxy)(file=file,filecontent=contents, project=project, version=version, build=build)
  return {"filename": file.filename}

@app.post('/upload/misc')
async def uploadMisc(
  # current_user: User = Depends(get_current_user),
  file: UploadFile = '',
  project: str = '',
  version: str = '',
  build: int = 0,
):
  contents = await file.read()

  await sync_to_async(uploadtoOther)(file=file,filecontent=contents, project=project, version=version, build=build)
  return {"filename": file.filename}