from django import forms


class ImageUploadForm(forms.ModelForm):
    class Meta:
        fields = [
            'image_link'
        ]
