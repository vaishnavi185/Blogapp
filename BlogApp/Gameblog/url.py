from django.urls import path
from .views import index_v, about_v, blog_list

urlpatterns = [
    path('', index_v, name='home'),
    path('about/', blog_list, name='about'),
]
