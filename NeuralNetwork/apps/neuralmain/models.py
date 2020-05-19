"""NeuralMain app models"""
import re

from datetime import datetime
# from django.contrib.auth import forms
from django.db import models
# from django import forms


def get_photo_group(self):
    """Returns the match name for a tag"""
    return re.sub("\W+" , "", self.photo_group.lower())


class PhotoRequest(models.Model):
    """ Request model
        photo_name: name of upload photo
        photo_date: datetime of upload photo
        photo_file: img file
    """
    photo_name = models.CharField("Имя фотографии", max_length=50, default='')
    photo_date = models.DateTimeField("Дата загрузки фото", default=datetime.now())
    photo_file = models.ImageField("Файл изображения", upload_to="requests/")


class PhotoToDatabase(models.Model):
    """ Model of the plant object sent to the database
        photo_name: name of upload photo
        photo_author: author of photo
        photo_group: type of plant
        photo_author_ip: author IP-address
        photo_date = models.DateTimeField("Дата и время загрузки фото", default='1111-11-11 11:11:11', max_length=25)
        photo_file = models.ImageField("Файл изображения", upload_to="img_to_database/")
    """
    photo_name = models.CharField("Имя фотографии", max_length=60, default='')
    photo_author = models.CharField("Автор фотографии", max_length=50)
    photo_group = models.CharField("Вид растения", max_length=20)
    photo_author_ip = models.GenericIPAddressField("ip адресс автора", default='0.0.0.0')
    photo_date = models.DateTimeField("Дата и время загрузки фото", default='1111-11-11 11:11:11', max_length=25)
    photo_file = models.ImageField("Файл изображения", upload_to="img_to_database/")

    def __str__(self):
        """ Function return string: Plant type | datetime"""
        return self.photo_group+"|"+str(self.photo_date)


class Auth(models.Model):
    """ Authentication model
        login_field: User login
        password_field: User password
    """
    login_field = models.CharField("Login", max_length=30)
    password_field = models.CharField(max_length=32)  # , widget=forms.PasswordInput
    # access_field = models.CharField(max_length=30, default='')


class Contacts(models.Model):
    """ Feedback model
         user_email: user email address
         message_field: user message
         author_ip: author IP-address
    """
    user_email = models.EmailField("Емаил пользователя")
    message_field = models.TextField("Сообщение", max_length=500)
    author_ip = models.GenericIPAddressField("ip адресс пользователя", default='0.0.0.0')

    def __str__(self):
        """ Function return user email"""
        return self.user_email




