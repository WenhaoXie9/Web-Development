from django.db import models

# Create your models here.
class Project(models.Model):
    indexId = models.AutoField(primary_key=True)
    #Sim_ID = models.AutoField(primary_key = True)
    Pixel_name = models.CharField(max_length=32)
    Size = models.CharField(max_length=32)
    True_w_h = models.CharField(max_length=32)
    K1_1 = models.FloatField()
    K2_1 = models.FloatField()
    A1P_1 = models.FloatField()
    A1_OS1 = models.CharField(max_length=32)
    A2P_1 = models.FloatField()
    A2_OS1 = models.CharField(max_length=32)
    Mesh_width = models.FloatField()
    A1_1 = models.FloatField()
    

    