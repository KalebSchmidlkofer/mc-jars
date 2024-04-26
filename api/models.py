from django.db import models

class jars(models.Model):
  type = models.CharField(max_length=300)
  version = models.CharField(max_length=20)
  build_number = models.IntegerField()
  commit = models.IntegerField()




