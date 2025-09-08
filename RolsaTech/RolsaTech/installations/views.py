from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Installation
from .forms import CreateInstallationForm

def create_installation(request, product_id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to access this page!')
        return redirect('home')

    if request.method == 'GET':
        form = CreateInstallationForm(user=request.user)
    else:
        form = CreateInstallationForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created installation!')
            return redirect('user_installations')

    return render(request, 'create_installation.html', {'form': form})

def edit_installation(request, installation_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to access this page!')
        return redirect('home')

    installation = get_object_or_404(Installation, pk=installation_id)

    if request.method == 'GET':
        form = CreateInstallationForm(instance=installation)
    else:
        form = CreateInstallationForm(request.POST, instance=installation)
        if form.is_valid():
            installation = form.save(commit=False)
            installation.user = request.user
            installation.save()

            messages.success(request, f'Successfully edited installation #{installation.id}!')
            return redirect('user_installations')

    return render(request, 'edit_installation.html', {'form': form})

def delete_installation(request, installation_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to access this page!')
        return redirect('home')

    installation = get_object_or_404(Installation, pk=installation_id)
    installation.delete()
    messages.success(request, 'Successfully deleted the installation!')
    return redirect('user_installations')
