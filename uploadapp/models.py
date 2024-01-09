from django.db import models

# Create your models here.
class Uploads(models.Model):
    image = models.ImageField(upload_to="images")
    #need to go to job setting.py to add property:MEDIA_ROOT = BASE_DIR / 'uploads'
    description = models.CharField(max_length=100)



class UploadFile(models.Model):
    file=models.FileField(upload_to="files")
    
    file_description = models.CharField(max_length=100)

def __str__(self):
    return self.description