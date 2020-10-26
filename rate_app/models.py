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
  phone_number = models.IntegerField()
  user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
  
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()  
 
class Project(models.Model):
  title =models.CharField(max_length=50)
  image = CloudinaryField('image')
  description = models.TextField()
  project_link = models.URLField(default='')
  user =models.ForeignKey(User,on_delete=models.CASCADE,default='',null=True)
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE,default='')
  
class Rating(models.Model):
  user =models.ForeignKey(User,on_delete=models.CASCADE,default='')
  project = models.ForeignKey(Project,on_delete=models.CASCADE,default='')  
  rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])