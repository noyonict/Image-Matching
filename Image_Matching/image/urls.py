from django.urls import path
from .views import index, all_images

urlpatterns = [
    path('all-images/', all_images, name='all-images'),
    path('', index, name='index-page'),
]
