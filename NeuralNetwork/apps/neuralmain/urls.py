"""List of page links and functions from views"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('upload/', views.upload, '', name='upload'),
    path('auth/', views.auth, name='auth'),
    path('contacts/', views.contacts, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += path('pattern/', views.pattern),
    # urlpatterns += path('database/', views.photo_in_database_list, name="database"),


