from django import forms
from .models import *


class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    exclude = ['user','profile']
    
class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']    
    
class RatingForm(forms.ModelForm):
  class Meta:
    model = Rating
    exclude = ['profile','project']