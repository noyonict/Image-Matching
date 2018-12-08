from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'Image Matching Portal'
    }
    return render(request, 'image/index.html', context)


def all_images(request):
    context = {
        'title': 'All Images'
    }
    return render(request, 'image/all-images.html', context)
