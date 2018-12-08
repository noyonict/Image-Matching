from django.shortcuts import render
from .models import UploadImage


# Create your views here.
def index(request):
    if request.method == 'POST':
        image_file = request.FILES['uploaded_image']
        UploadImage.objects.create(image_link=image_file)
    images = UploadImage.objects.order_by('-upload_at')
    context = {
        'title': 'Image Matching Portal',
        'images': images,
    }
    return render(request, 'image/index.html', context)


def all_images(request):
    images = UploadImage.objects.order_by('-upload_at')
    context = {
        'title': 'All Images',
        'images': images,
    }
    return render(request, 'image/all-images.html', context)
