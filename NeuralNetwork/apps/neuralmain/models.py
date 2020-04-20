import re

from datetime import datetime
from django.db import models


def get_photo_group(self):
    """Returns the match name for a tag"""
    return re.sub("\W+" , "", self.photo_group.lower())


class Contacts(models.Model):
    user_email = models.EmailField("Емаил пользователя")
    message_field = models.TextField("Сообщение", max_length=500)
    author_ip = models.GenericIPAddressField("ip адресс пользователя", default='0.0.0.0')


class PhotoRequest(models.Model):
    photo_name = models.CharField("Имя фотографии", max_length=50, default='')
    photo_date = models.DateTimeField("Дата загрузки фото", default=datetime.now())
    photo_file = models.ImageField("Файл изображения", upload_to="requests/")


class PhotoAnswer(models.Model):
    photo_name = models.CharField("Предположительный вид растения", max_length=200)
    photo_file = models.ImageField("Изображение предпологаемого вида")  # optional


class PhotoToDatabase(models.Model):
    photo_name = models.CharField("Имя фотографии", max_length=60, default='')
    photo_author = models.CharField("Автор фотографии", max_length=50)
    photo_group = models.CharField("Вид растения", max_length=20)
    photo_author_ip = models.GenericIPAddressField("ip адресс автора", default='0.0.0.0')
    photo_date = models.DateTimeField("Дата и время загрузки фото", default='1111-11-11 11:11:11', max_length=25)
    photo_file = models.ImageField("Файл изображения", upload_to="img_to_database/")

    def __str__(self):
        return self.photo_group+str(self.photo_date)


class PhotoInDatabase(models.Model):
    photo_name = models.CharField("Имя фотографии", max_length=50)
    photo_author = models.CharField("Автор фотографии", max_length=50)
    photo_group = models.CharField("Группа изображения", max_length=20)
    photo_date = models.DateTimeField("Дата загрузки фото")
    photo_file = models.ImageField("Файл изображения", upload_to="media/img")

    def __str__(self):
        return self.photo_name



