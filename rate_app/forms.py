from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    exclude = ['user']
    
class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']    