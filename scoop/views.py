from django.shortcuts import render, redirect
from .models import Product, RepairProduct
from .forms import ProductForm


def home(request):
    return render(request, 'scoop/home.html')


def sale(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'scoop/sale.html', context)


def sale_detail(request, pk):
    #product = get_object_or_404(Product, id=pk)
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return render(request, 'scoop/404.html')
    context = {
        'product' : product
    }
    return render(request, 'scoop/sale_detail.html', context)


def repairs(request):
    repairs = RepairProduct.objects.all()
    context = {
        'repairs': repairs
    }
    return render(request, 'scoop/repairs.html', context)


def about(request):
    return render(request, 'scoop/about.html')


def sale_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            """cd = form.cleaned_data
            Product.objects.create(
                title=cd['title'],
                description=cd['description'],
                price=cd['price'],
                image=cd['image'],
                author=cd['author']
            )"""
            form.save()
            return redirect(to='sale')
    else:
        form = ProductForm()
    
    context = {
        'form': form
    }
    return render(request, 'scoop/create.html', context)


def sale_delete(request, pk):
    products = Product.objects.get(id=pk)
    products.delete()
    return redirect(to='sale')


def sale_update(request, pk):
    products = Product.objects.get(id=pk)
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            author = form.cleaned_data['author']
            products.title = title
            products.description = description
            products.price = price
            products.image = image
            products.author = author
            products.save()
            return redirect(to='sale')
    context = {
        'form': form
    }
    return render(request, 'scoop/update.html', context)