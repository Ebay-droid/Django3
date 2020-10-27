from django.test import TestCase
from django.contrib.auth.models import User
from .models import *


# Create your tests here.
class  ProfileTest(TestCase):
  def setUp(self):
    user = User.objects.create(username='test',password = 'ugali')
    self.test = Profile(Bio='woohoo',user=user)
    
  def test_instance(self):
    self.assertTrue(isinstance(self.test,Profile))
    
    
class ProjectTest(TestCase):
   def setUp(self):
     user =User.objects.create(username='test',password='ugali')
     profile = Profile.objects.create(user=user,Bio='we gat this')   
    