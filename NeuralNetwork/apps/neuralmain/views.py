import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.files.storage import FileSystemStorage

from django.views.generic.base import View
from .forms import UploadFileForm  # PhotoFormUploadFileForm
from .models import Photo
from .img_handler import handle  # функция для обработки изображения
from .models import PhotoInDatabase
from NeuralNetwork.settings import BASE_DIR



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


# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})


def upload_file_main(request):
    # BASE_DIR_DATA_REQUESTS = BASE_DIR+"_Data\\requests"
    context = {}
    uploaded_file = None
    file = None
    if request.method == "POST":
        uploaded_file = request.FILES['img']
        if uploaded_file.multiple_chunks(chunk_size=10485760):
            file = uploaded_file.read()

        fs = FileSystemStorage()
        name = fs.save("requests\\"+uploaded_file.name, uploaded_file)  # BASE_DIR_DATA_REQUESTS+"\\"+
        url = fs.url(name)
        context = {'url': fs.url(name), "sdww": 225}
        print("File url:", url)
        print("Context", context)
        print("BASE_DIR:", BASE_DIR)
        # print("BASE_DIR_DATA_REQUESTS:", BASE_DIR_DATA_REQUESTS)
        print("OS.path:", os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+url)
        print("Big size upload file:", uploaded_file.multiple_chunks(chunk_size=10485760))
        print(context)
        # path = handle(url)
        # context['url'] = path

    return render(request, "website/main_upload.html", context)  # , 'img_name': uploaded_file.name #, {'file': file}
    # return render(request, "website/upload_doc.html")
