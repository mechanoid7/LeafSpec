import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.views.generic.base import View
from .forms import UploadFileForm  # PhotoFormUploadFileForm
from .models import Photo
from .img_handler import handle_uploaded_file  # функция для обработки изображения
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


def result(request):
    return render(request, 'website/main.html', {})


def index(request):
    return HttpResponse(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# class CheckLeaf(CreateView):  # новый
#     model = Photo
#     form_class = PhotoForm
#     template_name = 'main.html'
#     success_url = reverse_lazy('home')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def upload_file_main(request):
    if request.method == "POST":
        uploaded_file = request.FILES['img']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, "website/main_upload.html")
    # return render(request, "website/upload_doc.html")
