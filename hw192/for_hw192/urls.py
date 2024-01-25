from django.urls import path
from django.views.decorators.cache import cache_page
from for_hw192.views import BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, BlogCreateView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductListView

app_name = 'for_hw192'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<slug:slug>/', BlogDetailView.as_view(), name='view'),
    path('edit/<slug:slug>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<slug:pk>/', BlogDeleteView.as_view(), name='delete'),
    ###################################################################
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/view/<slug:slug>/', ProductDetailView.as_view(), name='view_product'),
    path('product/edit/<slug:slug>/', ProductUpdateView.as_view(), name='edit_product'),
    path('product/delete/<slug:pk>/', cache_page(60)(ProductDeleteView.as_view()), name='delete_product'),
    path('product/', ProductListView.as_view(), name='list_product'),
]

