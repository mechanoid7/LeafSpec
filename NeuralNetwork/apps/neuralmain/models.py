import re

from django.db import models


def get_photo_group(self):
    """Returns the match name for a tag"""
    return re.sub("\W+" , "", self.photo_group.lower())

class PhotoRequest(models.Model):
    photo_name = models.CharField("Имя фотографии", max_length=50)
    photo_date = models.DateTimeField("Дата загрузки фото")
    photo_file = models.ImageField("Файл изображения", upload_to="requests/")


class PhotoAnswer(models.Model):
    photo_name = models.CharField("Предположительный вид растения", max_length=200)
    photo_file = models.ImageField("Изображение предпологаемого вида")  # optional


class PhotoToDatabase(models.Model):
    # def get_photo_group(self):
    #     """Returns the match name for a tag"""
    #     return re.sub("\W+", "", self.photo_group.lower())

    photo_name = models.CharField("Имя фотографии", max_length=50)
    photo_author = models.CharField("Автор фотографии", max_length=50)
    photo_group = models.CharField("Вид растения", max_length=20)
    photo_author_ip = models.GenericIPAddressField("ip адресс автора")
    photo_date = models.DateTimeField("Дата загрузки фото")
    photo_file = models.ImageField("Файл изображения", upload_to="img_to_database/")  # +get_photo_group()+'/'
    # print(re.sub("\W+", "", photo_group.lower()))

    def __str__(self):
        return self.photo_name


class PhotoInDatabase(models.Model):
    photo_name = models.CharField("Имя фотографии", max_length=50)
    photo_author = models.CharField("Автор фотографии", max_length=50)
    photo_group = models.CharField("Группа изображения", max_length=20)
    photo_date = models.DateTimeField("Дата загрузки фото")
    photo_file = models.ImageField("Файл изображения", upload_to="media/img")

    def __str__(self):
        return self.photo_name



