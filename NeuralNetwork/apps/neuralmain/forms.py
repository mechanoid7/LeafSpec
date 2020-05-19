"""Forms to django output"""
from django import forms
from .models import PhotoToDatabase, PhotoRequest, Contacts, Auth


class PhotoRequestForm(forms.ModelForm):
    """Form to photo request"""
    class Meta:
        model = PhotoRequest
        fields = ('photo_file', 'photo_date')


class PhotoToDatabaseForm(forms.ModelForm):
    """Form to photo upload"""
    class Meta:
        model = PhotoToDatabase
        fields = ('photo_author', 'photo_group', 'photo_file', 'photo_author_ip', 'photo_name', 'photo_date')


class AuthForm(forms.ModelForm):
    """Form to auth"""
    class Meta:
        model = Auth
        fields = ('login_field', 'password_field')  # , 'access_field'


class ContactsForm(forms.ModelForm):
    """Form to contacts"""
    class Meta:
        model = Contacts
        fields = ('user_email', 'message_field', 'author_ip')
