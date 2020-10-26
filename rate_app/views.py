from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .forms import *
from .serializer import *
from rest_framework import status
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  return render(request, 'index.html')

@login_required
def profile(request,username):
  user = get_object_or_404(User,username=username)
  profile = Profile.objects.get(username=username)
  
  return render(request,'profile.html',{'user':user, 'profile':profile})

@login_required
def project(request):
  project = Project.objects.all()
  
  
  return render (request,'project.html',{'project':project})

@login_required
def project_detail(request,project_id):
  project = get_object_or_404(Project, id=project_id)
  
  
  return render (request, 'project_detail.html',{'project':project})

@login_required
def new_project(request):
  user = Profile.objects.get(user=request.user)
  if  request.method == 'POST':
    form = ProjectForm(request.POST, request.FILES)
    if form.is_valid():
      project =form.save(commit=False)
      project.profile = user
      project.user = request.user
      project.save()
    return redirect('project')  
  else:
    form = ProjectForm()
  return render (request, 'newproject.html',{'form':form})  
  
  
  
  
  
  
  
  
  return render (request,'')

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