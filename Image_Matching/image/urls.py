from django.urls import path
from .views import index, all_images, about_me

urlpatterns = [
    path('all-images/', all_images, name='all-images'),    # url 127.0.0.1:8000/all-images/
    path('about-me/', about_me, name='about-me'),          # url 127.0.0.1:8000/about-me/
    path('', index, name='index-page'),                    # url 127.0.0.1:8000
]
