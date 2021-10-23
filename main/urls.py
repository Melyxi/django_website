from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_folder, name="main"),
    path('<int:pk>/', views.get_folder, name="folder"),
    path('video/<int:pk>/', views.get_video, name='video')

]