from django.urls import path
from . import views


#move to views.py in app
# def hello(request):
#     return HttpResponse("Hello World")

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
     path('thank_you/', views.thank_you, name='thank_you')
   
]