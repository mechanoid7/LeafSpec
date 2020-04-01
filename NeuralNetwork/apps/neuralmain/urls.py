from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # path('neuro/', views.index, name='index'),
    # path('other/', views.main_page, name='other'),
    path('auth/', views.auth, name='auth'),
    path('contacts/', views.contacts, name='contacts'),
    # path('upload/', views.upload, name='upload'),
    path('upload/', views.upload, name='upload'),
    # path('result/', views.result),
    path('', views.main_user_request, name='upload_file_main'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += path('pattern/', views.pattern),
    # urlpatterns += path('database/', views.photo_in_database_list, name="database"),


