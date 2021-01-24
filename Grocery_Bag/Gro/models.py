from django.db import models

# Create your models here.
from django.db import models
# from datetime import datetime
# Create your models here.
class grocery(models.Model):
    iname = models.CharField(max_length=255,blank=True)
    quant = models.CharField(max_length=255,blank=True)
    status = models.CharField(max_length=255,blank=True)
    date=models.DateTimeField(auto_now_add=True,null=True)

