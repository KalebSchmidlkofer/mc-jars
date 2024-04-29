from django.db import models

JarTypes=['Servers', 'Proxies', 'Modded', 'Vanilla', 'Bedrock']
SoftwareTypes=[
  'Vanilla',
  'Paper',
  'Purpur',
  'Spigot',
  'CraftBukkit',
  'Tuinity',
  'Airplane',
  'Folia',
  'SpongeVanilla',
  'Glowstone',
  'Fabric',
  'Forge',
  'Crucible',
  'Cardboard',
  'Arclight',
  'Mohist',
  'Magma',
  'SpongeForge',
  'Waterfall',
  'Velocity',
  'Bungeecord',
  'Travertine',
  'GeyserMC',
  'TunnelMC']

class jars:
  type=models.CharField(choices=JarTypes)
  version=models.CharField(max_length=50)
  software=models.CharField(choices=SoftwareTypes)
  
