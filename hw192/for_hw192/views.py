from django.shortcuts import render

from for_hw192.models import Product


# Create your views here.

def index(request):
    all_products = Product.objects.all()
    context = {
        'object_list': all_products
    }
    print(context)
    return render(request, 'hw192/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')
    return render(request, 'hw192/contact.html')
