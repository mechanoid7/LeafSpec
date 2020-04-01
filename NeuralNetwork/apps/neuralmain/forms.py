from django import forms
from .models import PhotoInDatabase


# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()


class ImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
