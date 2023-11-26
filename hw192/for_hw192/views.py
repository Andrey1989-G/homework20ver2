from django.shortcuts import render, get_object_or_404

from for_hw192.models import Product


# Create your views here.

def index(request):
    all_products = Product.objects.all()
    print(all_products)
    context = {
        'object_list': all_products
    }
    print(context)
    return render(request, 'hw192/index.html', context)

def shop_single(request, prod_id): #prod_id передается из адресной строки. должен быть одинаков с path('shop-single/<slug:prod_id>
    one_product = get_object_or_404(Product, pk=prod_id)
    context = {
        'object_list': one_product
    }
    print(context)
    return render(request, 'hw192/shop-single.html', context)

def base(request):
    return render(request, 'hw192/base.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')
    return render(request, 'hw192/contact.html')
