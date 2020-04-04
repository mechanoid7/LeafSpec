from django import forms
from .models import PhotoToDatabase, PhotoRequest


# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()


class PhotoToDatabaseForm(forms.ModelForm):
    class Meta:
        model = PhotoToDatabase
        fields = ('photo_author', 'photo_group', 'photo_file', 'photo_author_ip', 'photo_name')  # , 'photo_author_ip', 'photo_name',        #'photo_date'


class PhotoRequestForm(forms.ModelForm):
    class Meta:
        model = PhotoRequest
        fields = ('photo_file',)
