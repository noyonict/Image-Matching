# Image-Matching
User can upload a png/jpg image and returns up to 3 of the most similar images that have already been uploaded

# Requirements
Python Version = 3.6.5

# Installation Guide
1. Install python 3.6.5 version
2. open terminal or cmd
3. Follow the commends
- virtualenv env
- cd env
- source bin/activate (in linux)
- Script/activate (in windows)
- mkdir src
- cd src
- git clone https://github.com/noyonict/Image-Matching.git
- cd Image-Matching/Image_Matching
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py makemigrations image
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
4. Then browse: 127.0.0.1:8000
5. For admin panel: 127.0.0.1:8000/admin/
6. All done
