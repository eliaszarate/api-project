from django.urls import path
from . import urls
from . import views

urlpatterns = [
    path('forms/', views.contact),
    #path('forms/', views.index, name='get_forms'),
    #path('jobs/', views.read_file, name ='read_jobs'),
    #path('jobs/links/', views.read_links, name ='read_links')
]

