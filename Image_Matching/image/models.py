from django.db import models


# For store user uploaded image
class UploadImage(models.Model):
    image_link = models.ImageField(upload_to='Images')
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image_link)
