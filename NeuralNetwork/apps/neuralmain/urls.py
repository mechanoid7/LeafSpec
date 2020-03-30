from django.urls import path
from . import views

urlpatterns = [
    path('neuro/', views.index, name='index'),
    # path('second/', views.second, name='second'),
    # path('', views.MainView.as_view()),
    path('other/', views.main_page),
    path('auth/', views.auth),
    path('contacts/', views.contacts),
    path('upload/', views.upload),
    path('result/', views.result),
    # path('identify/', views.Photo.as_view(), name='upload_photo_to_check'),
    path('', views.upload_file_main, name='upload_file_main'),
]
