# Image-Matching
User can upload a png/jpg image and returns up to 3 of the most similar images that have already been uploaded

# Requirements
Python Version = 3.6.5
Django==2.1.4
numpy==1.15.4
opencv-contrib-python==3.4.2.16
opencv-python==3.4.2.16
Pillow==5.3.0

# Installation Guide Using Dockerfile
1. Follow the commends
- git clone https://github.com/noyonict/Image-Matching.git
- cd Image-Matching
- docker-compose build
- docker-compose up
2. Then browse: 127.0.0.1:8800
4. All done

# Installation Guide Using Virtual Environment
1. Install python 3.6.5 version
2. open terminal or cmd
3. Follow the commends
- virtualenv env
- cd env
- source bin/activate (in linux)
- cd Scripts && activate && cd .. (in windows)
- mkdir src
- cd src
- git clone https://github.com/noyonict/Image-Matching.git
- cd Image-Matching
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py makemigrations image
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
4. Then browse: 127.0.0.1:8000
5. For admin panel: 127.0.0.1:8000/admin/
6. All done

# Technology Used
- os - Linux
- Programming Language - Python, JavaScript
- Framework - Django
- Library - OpenCV, numpy, Pillow, jQuery
- Database - SQLite3
- Web Server - Ngnix

# Image Similarity Algorithm Pseudocode & Description
def image_similarity_algorithm(original_image, all_other_images):
    key_point_1, descriptor_1 = from original_image
    top_three_images = []
    for image in all_other_images:
        key_point_2, descriptor_2 = from image
        matches = find the matches from (descriptor_1, descriptor_2)
        good_points = filter matches for good matches
        similarity_percentage = good_points / (low(key_point) * 100)
        compare similarity_percentage with top_three_images
        if similarity_percentage > top_three_images:
            replace similarity_percentage with top_three_images by its position
    return top_three_images
    
- SIFT (Scale-Invariant Feature Transform):
I used SIFT algorithm to find the key-points and descriptor from an image

- Feature Matching (FlannBasedMatcher.knnMatch):
For find the matches I used knnMatch. Which actually used Brute-Force matcher. 
Brute-Force matcher is simple. It takes the descriptor of one feature in first 
set and is matched with all other features in second set using some distance 
calculation. And the closest one is returned.

# Live Demo
http://image.pythonanywhere.com/
