from django.urls import path
from . import urls
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.read_file, name ='read_jobs'),
    path('jobs/links/', views.read_links, name ='read_links')
]

