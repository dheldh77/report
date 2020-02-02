from django.db import models

class Record(models.Model):
    fact = models.CharField(max_length=200,null=True) # 공장명
    line = models.CharField(max_length=200,null=True)  # 공정명
    date = models.DateTimeField(null=True)  # 장애시작시간
    maker = models.CharField(max_length=200,null=True) # maker
    model = models.CharField(max_length=200,null=True) # model
    part = models.CharField(max_length=200,null=True) # 장애부분
    fault = models.CharField(max_length=200,null=True) # fault 명
    cause = models.CharField(max_length=200,null=True) # 원인
    phenomenon = models.CharField(max_length=200,null=True) # 현상
    measure = models.CharField(max_length=200,null=True) # 조치내용

    def __str__(self):
        return self.fact

# Create your models here.
