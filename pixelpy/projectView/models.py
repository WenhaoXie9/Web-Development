from django.db import models

# Create your models here.
class Project(models.Model):
    indexId = models.AutoField(primary_key=True)
    