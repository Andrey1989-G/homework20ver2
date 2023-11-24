from django.urls import path
from django.conf import settings
from for_hw192.views import index, contact
from django.conf.urls.static import static

urlpatterns = [
    path('', index),
    path('contact/', contact)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

