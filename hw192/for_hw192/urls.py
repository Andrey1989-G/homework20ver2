from django.urls import path

from for_hw192.views import home, contacts

urlpatterns = [
    path('', home),
    path('contacts/', contacts)
]
