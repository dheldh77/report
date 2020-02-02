from django.db import models

class Record(models.Model):
    tmp1 = models.CharField(max_length=200,null=True)
    tmp2 = models.CharField(max_length=200,null=True) 
    tmp3 = models.CharField(max_length=200,null=True) 
    tmp4 = models.CharField(max_length=200,null=True) 
    tmp5 = models.CharField(max_length=200,null=True) 

# Create your models here.
