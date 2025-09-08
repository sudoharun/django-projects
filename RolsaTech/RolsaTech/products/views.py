from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import CreateProductForm

def create_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'You don\'t have permission to enter this page!')
        return redirect('home')

    if request.method == 'GET':
        form = CreateProductForm()
    else:
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created product!')
            return redirect('home')

    return render(request, 'create_product.html', {'form': form})

def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'You don\'t have permission to enter this page!')
        return redirect('home')

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'GET':
        form = CreateProductForm(instance=product)
    else:
        form = CreateProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully edited {product.name}!')
            return redirect('home')

    return render(request, 'edit_product.html', {'form': form})

def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'You don\'t have permission to enter this page!')
        return redirect('home')

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Successfully deleted the product!')
    return redirect('home')
