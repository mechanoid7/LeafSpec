"""NeuralMain app models"""
import re

from datetime import datetime
# from django.contrib.auth import forms
from django.db import models
# from django import forms


def get_photo_group(self):
    """Returns the match name for a tag
    Returns:
        - :photo_group: lowercase of type plants
    """
    return re.sub("\W+" , "", self.photo_group.lower())


class PhotoRequest(models.Model):
    """ Request model
    Parameters:
        - :photo_name(CharField): name of upload photo
        - :photo_date(DateTimeField): datetime of upload photo
        - :photo_file(ImageField): img file
    """
    photo_name = models.CharField("Имя фотографии", max_length=50, default='')
    photo_date = models.DateTimeField("Дата загрузки фото", default=datetime.now())
    photo_file = models.ImageField("Файл изображения", upload_to="requests/")

    def __str__(self):
        """ Function return string: Photo name | datetime"""
        return self.photo_name+"|"+str(self.photo_date)


class PhotoToDatabase(models.Model):
    """ Model of the plant object sent to the database
    Parameters:
        - :photo_name(CharField): name of upload photo
        - :photo_author(CharField): author of photo
        - :photo_group(CharField): type of plant
        - :photo_author_ip(GenericIPAddressField): author IP-address
        - :photo_date(DateTimeField): field for get Datetime(fill automatic)
        - :photo_file(ImageField): img file
    """
    photo_name = models.CharField("Имя файла", max_length=60, default='')
    photo_author = models.CharField("Автор фотографии", max_length=50)
    photo_group = models.CharField("Вид растения", max_length=20)
    photo_author_ip = models.GenericIPAddressField("ip-адрес автора", default='0.0.0.0')
    photo_date = models.DateTimeField("Дата и время загрузки фото", default='1111-11-11 11:11:11', max_length=25)
    photo_file = models.ImageField("Файл изображения", upload_to="img_to_database/")

    def __str__(self):
        """ Function for show in Adminpanel"""
        return f'{self.photo_group} — {str(self.photo_date.__format__("%d.%m // %H:%M | %Y"))} by "{self.photo_author}"'

class Auth(models.Model):
    """ Authentication model
    Parameters:
        - :login_field(CharField): User login
        - :password_field(CharField): User password
    """
    login_field = models.CharField("Login", max_length=30)
    password_field = models.CharField("Password", max_length=32)  # , widget=forms.PasswordInput
    login_date = models.DateTimeField("Дата и время авторизации", default='1111-11-11 11:11:11', max_length=25)
    # access_field = models.CharField("Контрольное поле", default=None, max_length=25)

    def __str__(self):
        """ Function for show in Adminpanel"""
        return f'{self.login_field} — {str(self.login_date.strftime("%d.%m // %H:%M | %Y"))}'


class Contacts(models.Model):
    """ Feedback model
    Parameters:
         - :user_email(EmailField): user email address
         - :message_field(TextField): user message
         - :author_ip(GenericIPAddressField): author IP-address
    """
    user_email = models.EmailField("Емаил пользователя")
    theme_field = models.CharField("Тема обращения", max_length=150)
    message_field = models.TextField("Сообщение", max_length=500)
    author_ip = models.GenericIPAddressField("ip адресс пользователя", default='0.0.0.0')

    def __str__(self):
        """ Function return user email + theme"""
        if len(self.user_email) > 35:
            # if email length more than 35 - make shorten
            email_splitted = self.user_email.split("@", 1)
            email = email_splitted[0][0:20]+'... @'+email_splitted[1]
        else: email = self.user_email
        return f'From: "{email}" — <{self.theme_field[0:35]}...>'
