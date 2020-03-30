from django.urls import path
from . import views

urlpatterns = [
    path('neuro/', views.index, name='index'),
    # path('second/', views.second, name='second'),
    # path('', views.MainView.as_view()),
    path('', views.main_page),
    path('auth/', views.auth),
    path('contacts/', views.contacts),
    path('upload/', views.upload),
]
