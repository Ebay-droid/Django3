from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
  title =models.CharField(max_length=50)
  image = CloudinaryField('image')
  description = models.TextField()
  project_link = models.URLField(default='')
  
class  Profile(models.Model):
  profile_pic = CloudinaryField('image')
  Bio = models.TextField()
  email = models.EmailField()
  phone_number = models.IntegerField()
  project = models.ForeignKey(Project,on_delete=models.CASCADE)
  user = models.ForeignKey(User,on_delete=models.CASCADE,default='')