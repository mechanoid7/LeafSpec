import os

from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.base import View
from .models import PhotoInDatabase


# from .models import PhotoAnswer


class MainView(View):  # available links
    """ Вывод ответа """
    def get(self, request):
        photos = PhotoInDatabase.objects.all()
        # photos = ["123", "456", "789"]
        # return render(request, "HTML_sites/main.html", {"photos": photos})
        return render(request, "website/main.html", {"photos": photos})


def auth(request):
    return render(request, 'website/auth.html', {})


def contacts(request):
    return render(request, 'website/contacts.html', {})


def main_page(request):
    return render(request, 'website/main.html', {})


def upload(request):
    return render(request, 'website/upload.html', {})


def index(request):
    return HttpResponse(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
