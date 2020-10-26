from  django.urls import path
from . import views



urlpatterns =[
  path('', views.index, name = 'index'),
  path('project/', views.project, name = 'project'),
  path('project/<project_id>/rating', views.rating, name = 'rating'),
  path('project/<project_id>/', views.project_detail, name = 'project_detail'),
  path('new_project/', views.new_project, name = 'new_project'),
  path('profile/<username>/', views.profile, name = 'profile'),
  path('new_profile/<username>/', views.update_profile, name = 'new_profile'),
  path('api/profiles/', views.ProfileList.as_view()),
  path('api/projects/', views.ProjectList.as_view()),
  
  
]