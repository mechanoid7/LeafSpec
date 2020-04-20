from django import forms
from .models import PhotoToDatabase, PhotoRequest, Contacts


class PhotoToDatabaseForm(forms.ModelForm):
    class Meta:
        model = PhotoToDatabase
        fields = ('photo_author', 'photo_group', 'photo_file', 'photo_author_ip', 'photo_name', 'photo_date')


class PhotoRequestForm(forms.ModelForm):
    class Meta:
        model = PhotoRequest
        fields = ('photo_file', 'photo_date')


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('user_email', 'message_field', 'author_ip')
