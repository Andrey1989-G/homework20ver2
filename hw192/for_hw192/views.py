from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from for_hw192.models import Blog, Product, Version

from for_hw192.forms import ProductForm, VersionForm


# Create your views here.

class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'img_preview', 'sign_publication',) #здесь устанавливаются поля для автоматической формы
    success_url = reverse_lazy('for_hw192:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

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
        """ добавили счетик просмотров """
        self.object = super().get_object(queryset)
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

###################################################################
#crud для продуктов
###################################################################

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('for_hw192:list_product')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.product_name)
            new_product.save()
        return super().form_valid(form)

class ProductListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset

class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('for_hw192:list_product')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('for_hw192:list_product')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('for_hw192:list_product')


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
