from  django.urls import path
from . import views



urlpatterns =[
  path('', views.index, name = 'index'),
  path('project/', views.project, name = 'project'),
  path('project/<project_id>/', views.project_detail, name = 'project_detail'),
  path('new_project/', views.project, name = 'new_project'),
  path('profile/', views.profile, name = 'profile'),
  path('api/profiles/', views.ProfileList.as_view()),
  path('api/projects/', views.ProjectList.as_view()),
  
]