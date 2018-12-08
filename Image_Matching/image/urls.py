from django.urls import path
from .views import index, all_images, about_me

urlpatterns = [
    path('all-images/', all_images, name='all-images'),
    path('about-me/', about_me, name='about-me'),
    path('', index, name='index-page'),
]
