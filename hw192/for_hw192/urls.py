from django.urls import path
from for_hw192.views import BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, BlogCreateView

app_name = 'for_hw192'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<slug:slug>/', BlogDetailView.as_view(), name='view'),
    path('edit/<slug:slug>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<slug:pk>/', BlogDeleteView.as_view(), name='delete'),
]

