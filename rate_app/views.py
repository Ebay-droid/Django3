from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .forms import *
from .serializer import *
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.urls import  reverse
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def index(request):
  return render(request, 'index.html')

@login_required
def profile(request,username):
  user = get_object_or_404(User,username=username)
  profile = Profile.objects.get(user=user)
  
  return render(request,'profile.html',{'user':user, 'profile':profile})

@login_required
def project(request):
  project = Project.objects.all()
  
  
  return render (request,'project.html',{'project':project})

@login_required
def project_detail(request,project_id):
  user = request.user
  project = get_object_or_404(Project, id=project_id)
  profile = Profile.objects.get(Profile,user=user)
  


  
  return render (request, 'project_detail.html',{'project':project, 'user':user,'profile':profile})

@login_required
def rating(request,project_id):
  user = request.user
  project = get_object_or_404(Project, id=project_id)
  profile = Profile.objects.get(Profile,user=user)

  if request.method == 'POST':
      form = RatingForm(request.POST)
      if form.is_valid():
        rating = form.save(commit=False)
        rating.project = project
        rating.profile = profile
        rating.save()
      return redirect('project_detail')  
  else:
    form = RatingForm()
  return render(request, 'rate.html'{'form':form})  
    
    
    
      

@login_required
def new_project(request):
  user = request.user
  profile = Profile.objects.get(user=request.user)
  
  if  request.method == 'POST':
    form = ProjectForm(request.POST, request.FILES)
    if form.is_valid():
      project =form.save(commit=False)
      project.profile = profile
      project.user = request.user
      project.save()
    return redirect('project')  
  else:
    form = ProjectForm()
  return render (request, 'newproject.html',{'form':form})  
  
@login_required
def update_profile(request, username):
  user = get_object_or_404(User,username=username)  
  new_user = request.user
  if request.method == 'POST':
    
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = new_user
      profile.save()
      
      return HttpResponseRedirect(reverse('profile', args=[username]))
    else:
      form = ProfileForm()
    
  return render(request, 'new_profile.html',{'user':user,'form':ProfileForm})   
  

class ProfileList(APIView):
  def get(self, request, format=None):
    profiles = Profile.objects.all()
    serializers = ProfileSerializer(profiles, many=True)
    return Response(serializers.data)

  def post(self, request,format=None):
    serializers = ProfileSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
class ProjectList(APIView):
  def get(self,request,format=None):
    projects = Project.objects.all()
    serializers = ProjectSerializer(projects,many=True)
    return Response(serializers.data)
  
  def post(self,request,format=None):
    serializers=ProjectSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)  