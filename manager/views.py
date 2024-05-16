from django.shortcuts import render
from django.http import HttpResponse
from .models import SoftwareTypes, jar, servers, modded, vanilla, bedrock, proxies, other
from django.core.files.uploadedfile import SimpleUploadedFile


def jarInstance(file, filecontent, project, version, build, software):
  file = SimpleUploadedFile(f'{project}-{version}-{build}.jar', filecontent)
  jarInstance = jar.objects.create(
    title=f'{project}-{version}',
    project=project,
    version=version,
    software=software,
    buildnum=build,
    posted=True,  
    experimental=False, 
    file=file  
  )
  jarInstance.save()
  return jarInstance

def uploadtoServer(file, filecontent, project, version, build):
  Instance=jarInstance(file, filecontent, project, version, build, 'Servers')
  
  serverInstance = servers.objects.create(
    project=Instance
  )
  serverInstance.save()

def uploadtoModded(file, filecontent, project, version, build):
  Instance=jarInstance(file, filecontent, project, version, build, 'Modded')
  
  serverInstance = modded.objects.create(
    project=Instance
  )
  serverInstance.save()

def uploadtoProxy(file, filecontent, project, version, build):
  Instance=jarInstance(file, filecontent, project, version, build, 'Proxies')
  
  serverInstance = proxies.objects.create(
    project=Instance
  )
  serverInstance.save()

def uploadtoVanilla(file, filecontent, project, version, build):
  Instance=jarInstance(file, filecontent, project, version, build, 'Vanilla')
  
  serverInstance = vanilla.objects.create(
    project=Instance
  )
  serverInstance.save()

def uploadtoBedrock(file, filecontent, project, version, build):
  Instance=jarInstance(file, filecontent, project, version, build, 'Bedrock')
  
  serverInstance = bedrock.objects.create(
    project=Instance
  )
  serverInstance.save()

def uploadtoOther(file, filecontent, project, version, build):
  Instance=jarInstance(file, filecontent, project, version, build, 'Misc')
  
  serverInstance = other.objects.create(
    project=Instance
  )
  serverInstance.save()

