"""
URL configuration for job project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
# from django.http import HttpResponse
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


#move to views.py in app
# def hello(request):
#     return HttpResponse("Hello World")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('app.urls')),
    # path('', hello),  #delete it and move to urls.py in app
    #but add path directing to app.urls
    path('', include('subscribe.urls')),
    path('uploads/', include('uploadapp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#the static things help to show image after its get verified or saved
#add MEDIA_URL/ROOT in job settings.py
