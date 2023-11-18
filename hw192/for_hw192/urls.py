from django.urls import path
from django.conf import settings
from for_hw192.views import home, contacts
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('contacts/', contacts)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
