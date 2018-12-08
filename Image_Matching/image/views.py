from django.shortcuts import render
from .models import UploadImage


# Create your views here.
def index(request):
    images = UploadImage.objects.order_by('-upload_at')
    new_image = None
    if request.method == 'POST':
        image_file = request.FILES['uploaded_image']
        new_image = UploadImage.objects.create(image_link=image_file)
        images = images.exclude(id=new_image.id)
    context = {
        'title': 'Image Matching Portal',
        'images': images,
        'new_image': new_image,
    }
    return render(request, 'image/index.html', context)


def all_images(request):
    images = UploadImage.objects.order_by('-upload_at')
    context = {
        'title': 'All Images',
        'images': images,
    }
    return render(request, 'image/all-images.html', context)
