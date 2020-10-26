from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework import status


# Create your views here.
def index(request):
  return render(request, 'index.html')

def profile(request):
  return render(request,'profile.html')

def project(request):
  return render (request,'projects.html')

def project_detail(request):
  return render (request, 'project_detail.html')

def new_project(request):
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