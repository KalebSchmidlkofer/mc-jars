from django.shortcuts import render
from django.http import HttpResponse
from .models import jar, servers, modded, vanilla, bedrock, proxies, other
from django.core.files.uploadedfile import SimpleUploadedFile

def uploadtoServer(file, filecontent, project, version, build):
  file = SimpleUploadedFile(f'{project}-{version}-{build}.jar', filecontent)
  jarInstance = jar.objects.create(
    title=f'{project}-{version}',
    project=project,
    version=version,
    software='Servers',
    buildnum=build,
    posted=True,  
    experimental=False, 
    file=file  
  )

  serverInstance = servers.objects.create(
    project=jarInstance
  )
  jarInstance.save()
  serverInstance.save()


