from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from for_hw192.models import Blog

# Create your views here.

class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'img_preview', 'sign_publication', 'number_views',)
    success_url = reverse_lazy('for_hw192:list')

class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_publication=True)
        return queryset

class BlogDetailView(DetailView):
    model = Blog
    success_url = reverse_lazy('for_hw192:list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.number_views is None:
            self.object.number_views == 1
        else:
            self.object.number_views += 1
        self.object.save()
        return self.object

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'img_preview', 'sign_publication', 'number_views',)
    success_url = reverse_lazy('for_hw192:list')

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('for_hw192:list')

# class IndexListView(ListView):
#     model = Product
#     template_name = 'for_hw192/index.html'
#
# class ShopSingleDetailView(DetailView):
#     model = Product
#     template_name = 'for_hw192/shop-single.html'

# def index(request):
#     all_products = Product.objects.all()
#     print(all_products)
#     context = {
#         'object_list': all_products
#     }
#     print(context)
#     return render(request, 'hw192/index.html', context)

# def shop_single(request, prod_id): #prod_id передается из адресной строки. должен быть одинаков с path('shop-single/<slug:prod_id>
#     one_product = get_object_or_404(Product, pk=prod_id)
#     context = {
#         'object_list': one_product
#     }
#     print(context)
#     return render(request, 'hw192/shop-single.html', context)

# def base(request):
#     return render(request, 'for_hw192/base.html')
#
# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name}, {phone}, {message}')
#     return render(request, 'for_hw192/contact.html')
