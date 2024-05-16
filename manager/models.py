from django.db import models
import hashlib
from os import path
from jars.settings import MEDIA_ROOT

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
  ('Purformance', 'Purformance'),
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
  return upload_to(instance, filename)

class jar(models.Model):
  title = models.CharField(max_length=50, unique=True, default=None)
  project=models.CharField(choices=Types, max_length=50)
  version=models.CharField(max_length=50)
  software=models.CharField(choices=SoftwareTypes, max_length=50)
  buildnum=models.IntegerField(default=0)
  posted=models.BooleanField(default=True)
  experimental=models.BooleanField(default=False)
  file = models.FileField(upload_to=get_upload_to)
  file_size = models.CharField(null=True, blank=True, editable=False, max_length=50)
  file_hash=models.CharField(max_length=200, editable=False, blank=True, null=True)
  date_added=models.DateTimeField(auto_now=False, auto_now_add=True)

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    # Calculate file size and convert it to a readable format
    if self.file:
      size = self.file.size
      if size < 1024:
        self.file_size = f"{size} bytes"
      elif size < 1024 * 1024:
        self.file_size = f"{size / 1024:.2f} KB"
      elif size < 1024 * 1024 * 1024:
        self.file_size = f"{size / (1024 * 1024):.2f} MB"
      else:
        self.file_size = f"{size / (1024 * 1024 * 1024):.2f} GB"
      self.file_hash=hashlib.md5(open(self.file.path, 'rb').read()).hexdigest()
    super().save(update_fields=['file_size', 'file_hash'])
  
  def __str__(self):
    return self.title
  class Meta:
    verbose_name_plural = "Jars"

class servers(models.Model):
  project=models.ForeignKey(jar, on_delete=models.CASCADE, related_name='Server')
  def __str__(self):
    return self.project.title

  class Meta:
    verbose_name_plural="servers"

class bedrock(models.Model):
  project=models.ForeignKey(jar, on_delete=models.CASCADE, related_name='Bedrock')
  
  def __str__(self):
    return self.project.title
  class Meta:
    verbose_name_plural="bedrock"

class modded(models.Model):
  project=models.ForeignKey(jar, on_delete=models.CASCADE, related_name='Modded')
  
  def __str__(self):
    return self.project.title
  class Meta:
    verbose_name_plural="modded"

class vanilla(models.Model):
  project=models.ForeignKey(jar, on_delete=models.CASCADE, related_name='Vanilla')
  
  def __str__(self):
    return self.project.title
  class Meta:
    verbose_name_plural="vanilla"

class proxies(models.Model):
  project=models.ForeignKey(jar, on_delete=models.CASCADE, related_name='Proxy')
  
  def __str__(self):
    return self.project.title
  class Meta:
    verbose_name_plural="proxies"


def upload_to(instance: jar, filename):
  # Ensure that only allowed characters are included in the filename
  filename = path.basename(filename)
  
  # Construct the upload path using safe directory joining method
  upload_path = path.join(
    instance.project,
    instance.software,
    filename
  )
  
  # Return the sanitized upload path
  return upload_path
