from django.urls import path
from . import views


urlpatterns = [
    path('images/', views.image_upload, name='image_upload'),
    path('files/', views.file_upload, name='file_upload')
]