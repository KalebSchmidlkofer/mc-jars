from django.db import models
from os import path
Types = [
  ('Servers', 'Servers'),
  ('Proxies', 'Proxies'),
  ('Modded', 'Modded'),
  ('Vanilla', 'Vanilla'),
  ('Bedrock', 'Bedrock')
]

SoftwareTypes = [
  ('Vanilla', 'Vanilla'),
  ('Paper', 'Paper'),
  ('Purpur', 'Purpur'),
  ('Spigot', 'Spigot'),
  ('CraftBukkit', 'CraftBukkit'),
  ('Tuinity', 'Tuinity'),
  ('Airplane', 'Airplane'),
  ('Folia', 'Folia'),
  ('SpongeVanilla', 'SpongeVanilla'),
  ('Glowstone', 'Glowstone'),
  ('Fabric', 'Fabric'),
  ('Forge', 'Forge'),
  ('Crucible', 'Crucible'),
  ('Cardboard', 'Cardboard'),
  ('Arclight', 'Arclight'),
  ('Mohist', 'Mohist'),
  ('Magma', 'Magma'),
  ('SpongeForge', 'SpongeForge'),
  ('Waterfall', 'Waterfall'),
  ('Velocity', 'Velocity'),
  ('Bungeecord', 'Bungeecord'),
  ('Travertine', 'Travertine')
]

def get_upload_to(instance, filename):
    # Use the 'software' field of the instance to create the upload path
    return path.join('uploads', instance.type, instance.software, filename)

class jars(models.Model):
  title = models.CharField(max_length=50, unique=True, default=None)
  type=models.CharField(choices=Types, max_length=50)
  version=models.CharField(max_length=50)
  software=models.CharField(choices=SoftwareTypes, max_length=50)
  buildnum=models.IntegerField()
  posted=models.BooleanField(default=True)
  file = models.FileField(upload_to=get_upload_to)
  date_added=models.DateTimeField(auto_now=False, auto_now_add=True)


class servers(models.Model):
  type=models.ForeignKey(jars, on_delete=models.CASCADE, related_name='Server')

class bedrock(models.Model):
  type=models.ForeignKey(jars, on_delete=models.CASCADE, related_name='Bedrock')

class modded(models.Model):
  type=models.ForeignKey(jars, on_delete=models.CASCADE, related_name='Modded')

class vanilla(models.Model):
  type=models.ForeignKey(jars, on_delete=models.CASCADE, related_name='Vanilla')

class proxies(models.Model):
  type=models.ForeignKey(jars, on_delete=models.CASCADE, related_name='Proxy')


