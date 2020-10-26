from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class  Profile(models.Model):
  profile_pic = CloudinaryField('image')
  Bio = models.TextField()
  email = models.EmailField()
  phone_number = models.IntegerField(null=True)
  user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
  
  
  def __str__(self):
    return self.user.username
  
  def save_profile(self):
    self.save()
  
 
class Project(models.Model):
  title =models.CharField(max_length=50)
  image = CloudinaryField('image')
  description = models.TextField()
  project_link = models.URLField(default='')
  user =models.ForeignKey(User,on_delete=models.CASCADE,default='',null=True)
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE,default='')
  
  def save_project(self):
    self.save()
    
  def delete_project(self):
    self.delete()  
  
  def __str__(self):
      return self.title 
  
class Rating(models.Model):
  profile =models.ForeignKey(Profile,on_delete=models.CASCADE,default='')
  project = models.ForeignKey(Project,on_delete=models.CASCADE,default='')  
  design = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
  usability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
  content = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
  