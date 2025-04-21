from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import get_request_info, upload_file

urlpatterns = [
    path('request-info/', get_request_info, name='request_info'),
    path('upload-file/', upload_file, name='upload_file'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)