import cv2
from django.shortcuts import render
from .models import UploadImage
from .forms import ImageUploadForm


def find_similar_images(original_image, all_image_to_compare):
    """
    Compare one image from a list of image and return top 3 similar images
    :param original_image: A UploadImage Object
    :param all_image_to_compare: List of UploadImage objects except original_image object
    :return: Top 3 similar images as like original_image from all_image_to_compare
    """
    original = cv2.imread(original_image.image_link.path)  # Read Original Image
    sift = cv2.xfeatures2d.SIFT_create()  # Initialize SIFT algorithm
    kp1, desc_1 = sift.detectAndCompute(original, None)  # Find the Key point and Descriptors from original image
    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)  # Initialize FlannBasedMatcher object

    top_three_images = []
    first = 0
    second = 0
    third = 0
    for f in all_image_to_compare:  # Loop throw all other images one by one
        image_to_compare = cv2.imread(f.image_link.path)  # Read other image
        kp2, desc_2 = sift.detectAndCompute(image_to_compare,
                                            None)  # Find the Key-point and Descriptors from other image

        matches = flann.knnMatch(desc_1, desc_2, k=2)  # Find the matches of two images

        good_points = []
        for m, n in matches:  # Loop throw all matches and find good points
            if m.distance < 0.7 * n.distance:
                good_points.append(m)

        if len(kp1) >= len(kp2):  # Initialize number_keypoints by lower key-points
            number_keypoints = len(kp2)
        else:
            number_keypoints = len(kp1)

        similarity = len(good_points) / number_keypoints * 100  # Calculate similarity percentage
        if similarity > first:          # Compare Similarity percentage with first
            top_three_images.insert(0, f)
            first = similarity
        elif similarity > second:  # Compare Similarity percentage with second
            top_three_images.insert(1, f)
            second = similarity
        elif similarity > third:  # Compare Similarity percentage with third
            if len(top_three_images) > 2:  # if Similarity percentage is bigger then replace it
                top_three_images.pop(2)
            top_three_images.insert(2, f)
            third = similarity
    return top_three_images[:3]  # Return top 3 images


# Create your views here.
def index(request):
    """
    Home page of this web
    :param request: HTTP Request object
    :return: Home page with title and all Image objects
    """
    images = UploadImage.objects.order_by('-upload_at')
    new_image = None
    error = ''
    try:
        if request.method == 'POST':
            image_file = request.FILES['uploaded_image']  # get the user uploaded image
            new_image = UploadImage.objects.create(image_link=image_file)  # create new UploadImage Object
            images = images.exclude(id=new_image.id)  # All images except new image
            images = find_similar_images(new_image, images)  # Call the find_similar_images object
    except Exception as e:
        error = 'Uploaded file is not an Image or an corrected Image. Please upload a image ...' + str(e)
    context = {
        'title': 'Image Matching Portal',
        'images': images,
        'new_image': new_image,
        'error': error
    }
    return render(request, 'image/index.html', context)


def all_images(request):
    """
    All Images ar listed here
    :param request: A Request Object
    :return: all image.html with all image objects
    """
    images = UploadImage.objects.order_by('-upload_at')
    context = {
        'title': 'All Images',
        'images': images,
    }
    return render(request, 'image/all-images.html', context)


def about_me(request):
    """
    About me page with developer information
    :param request: A Request Object
    :return: about me page
    """
    context = {
        'title': 'Md. Mohaymenul Islam (Noyon)',
    }
    return render(request, 'about-me.html', context)
