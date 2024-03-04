from django.db import models

# Create your models here.
class imagedata(models.Model):
    imagename=models.CharField(max_length=50)
    image=models.ImageField(upload_to='img/')
