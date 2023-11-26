from django.urls import path
from django.conf import settings
from for_hw192.views import index, contact, shop_single, base
from django.conf.urls.static import static

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('shop-single/<slug:prod_id>/', shop_single, name='one_product'),
    path('base/', base)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

