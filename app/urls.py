from django.urls import path
# from app.views import hello, job_detail
from app import views

#from . import views 
#. means current folder

urlpatterns = [  
    path('', views.job_list, name='jobs_home'),
    path('hello/', views.hello, name='hello'),
    # path('job/1', views.job_detail),
    path('job/<int:id>', views.job_detail, name='job_detail'),
    # path('job/<str:id>', views.job_detail),
    # path('job_list', views.job_list, name)
]
