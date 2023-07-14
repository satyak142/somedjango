from django.shortcuts import render
from .models import Product

# Create your views here.
from .forms import ProductForm


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.desciption
    # }
    context = {
        'object': obj
    }
    return render(request, 'product/detail.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'product/create.html', context)
