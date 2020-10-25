from rest_framework import serializers
from .models import *


class  ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('title','description','omage','project_link')
    
    
class  ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields =  ('profile_pic','Bio','email','phone-number',)   