from django.urls import path
from . import views
urlpatterns = [
    path('',views.projects,name="projects"),
    path('project/<str:kp>/',views.project,name="project"),
    path('create-project/',views.createProject,name="create-project"),
    path('update-project/<str:kp>/',views.updateProject,name="update-project"),
    path('delete-project/<str:kp>/',views.deleteProject,name='delete-project'),


]
