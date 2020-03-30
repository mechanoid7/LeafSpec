from django.db import models


class Photo(models.Model):
    photo_name = models.CharField("Имя фотографии", max_length=50)
    photo_date = models.DateTimeField("Дата загрузки фото")
    # photo_file = models.FileField("Файл изображения")
    photo_file = models.ImageField("Файл изображения", upload_to="media/requests")


class PhotoAnswer(models.Model):
    photo_name = models.CharField("Предположительный вид растения", max_length=200)
    photo_file = models.ImageField("Изображение предпологаемого вида")


class PhotoToDatabase(models.Model):
    photo_name = models.CharField("Имя фотографии", max_length=50)
    photo_author = models.CharField("Автор фотографии", max_length=50)
    photo_group = models.CharField("Группа изображения", max_length=20)
    photo_author_ip = models.GenericIPAddressField("ip адресс автора")
    photo_date = models.DateTimeField("Дата загрузки фото")
    photo_file = models.ImageField("Файл изображения", upload_to="media/user_img")


class PhotoInDatabase(models.Model):
    photo_name = models.CharField("Имя фотографии", max_length=50)
    photo_author = models.CharField("Автор фотографии", max_length=50)
    photo_group = models.CharField("Группа изображения", max_length=20)
    photo_date = models.DateTimeField("Дата загрузки фото")
    photo_file = models.ImageField("Файл изображения", upload_to="media/img")


