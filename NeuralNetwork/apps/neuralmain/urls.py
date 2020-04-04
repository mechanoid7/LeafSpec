from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('contacts/', views.contacts, name='contacts'),
    path('upload/', views.upload, '', name='upload'),
    # path('', views.main_user_request, name='main_user_request'),
    path('', views.main, name='upload_file_main'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += path('pattern/', views.pattern),
    # urlpatterns += path('database/', views.photo_in_database_list, name="database"),


