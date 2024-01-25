from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from for_hw192.services import get_cached_category_list

from for_hw192.models import Blog, Product, Version

from for_hw192.forms import ProductForm, VersionForm, ProductFormModerator, ProductFormUser


# Create your views here.

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'content', 'img_preview', 'sign_publication',) #здесь устанавливаются поля для автоматической формы
    success_url = reverse_lazy('for_hw192:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

class BlogListView(LoginRequiredMixin, ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_publication=True)
        return queryset

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    success_url = reverse_lazy('for_hw192:list')

    def get_object(self, queryset=None):
        """ добавили счетик просмотров """
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'img_preview', 'sign_publication', 'number_views',)
    success_url = reverse_lazy('for_hw192:list')

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('for_hw192:list')

###################################################################
#crud для продуктов
###################################################################

class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('for_hw192:list_product')
    permission_required = 'for_hw192:create_product'

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.product_name)
            new_product.save()
        return super().form_valid(form)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    success_url = reverse_lazy('for_hw192:list_product')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            key = f'subject_list{self.object.pk}'
            subject_list = cache.get(key)
            if subject_list is None:
                subject_list = self.object.subject_set.all()
                cache.set(key, subject_list)
        else:
            subject_list = self.object.subject_set.all()

        context_data['subject'] = subject_list
        return context_data

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('for_hw192:list_product')
    permission_required = 'for_hw192:edit_product'

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

    def get_form_class(self):
        if self.request.user.groups.filter("moderator"):
            return ProductFormModerator
        else:
            return ProductFormUser

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner == self.request.user or self.request.user.groups.filter("moderator") or self.request.user.is_superuser:
            return self.object
        else:
            raise Http404("Доступ закрыт")


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('for_hw192:list_product')

    def test_func(self):
        return self.request.user.is_superuser

class HomeView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная',
        'description': 'Вся информация о товаре',
    }
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        for product in queryset:
            version = product.version_set.all().filter(is_current=True).first()
            product.version = version

        return queryset