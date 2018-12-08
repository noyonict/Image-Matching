from django.shortcuts import render
from .models import UploadImage
import cv2


def find_similar_images(original_image, all_image_to_compare):
    original = cv2.imread(original_image.image_link.path)
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, disc_1 = sift.detectAndCompute(original, None)
    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    top_three_images = []
    first = 0
    second = 0
    third = 0
    for f in all_image_to_compare:
        image_to_compare = cv2.imread(f.image_link.path)
        kp2, disc_2 = sift.detectAndCompute(image_to_compare, None)

        matches = flann.knnMatch(disc_1, disc_2, k=2)

        good_points = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good_points.append(m)

        if len(kp1) >= len(kp2):
            number_keypoints = len(kp2)
        else:
            number_keypoints = len((kp1))

        similarity = len(good_points) / number_keypoints * 100
        if similarity > first:
            if top_three_images:
                top_three_images.pop(0)
            top_three_images.insert(0, f)
            first = similarity
        elif similarity > second:
            if len(top_three_images) > 1:
                top_three_images.pop(1)
            top_three_images.insert(1, f)
            second = similarity
        elif similarity > third:
            if len(top_three_images) > 2:
                top_three_images.pop(2)
            top_three_images.insert(2, f)
            third = similarity
    return top_three_images


# Create your views here.
def index(request):
    images = UploadImage.objects.order_by('-upload_at')
    new_image = None
    if request.method == 'POST':
        image_file = request.FILES['uploaded_image']
        new_image = UploadImage.objects.create(image_link=image_file)
        images = images.exclude(id=new_image.id)
        images = find_similar_images(new_image, images)
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
