from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm, LoginForm
from installations.models import Installation
from consultations.models import Consultation

def sign_up(request):
    if request.method == "GET":
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully signed up and logged in!')
                return redirect('home')
            else:
                messages.error(request, 'Authentication failed. Please log in manually.')
                return redirect('home')

    return render(request, 'signup.html', {'form': form})

def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged in!')
                return redirect('home')
            else:
                messages.error(request, 'There was an error logging you in')

    return render(request, 'login.html', {'form': form})

def log_out(request):
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return redirect('home')

def edit_account(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to access this page!')
        return redirect('home')

    if request.method == 'GET':
        form = CustomUserChangeForm(instance=request.user)
    else:
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited account information!')

    return render(request, 'edit_account.html', {'form': form})

def change_password(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to access this page!')
        return redirect('home')

    if request.method == 'GET':
        form = CustomPasswordChangeForm(user=request.user)
    else:
        form = CustomPasswordChangeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully changed password!')

    return render(request, 'change_password.html', {'form': form})

def delete_account(request):
    return render(request, 'confirm_account_deletion.html', {})

def account_deletion_confirmed(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to access this page!')
        return redirect('home')

    user = request.user
    logout(request)
    user.delete()
    messages.success(request, 'Account successfully deleted!')
    return redirect('home')

def consultations(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to access this page!')
        return redirect('home')

    if request.user.is_superuser:
        all_consultations = Consultation.objects.all()
    else:
        all_consultations = None

    consultations = request.user.consultation_set.all()
    return render(request, 'consultations.html', {'consultations': consultations, 'all_consultations': all_consultations})

def installations(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to access this page!')
        return redirect('home')

    if request.user.is_superuser:
        all_installations = Installation.objects.all()
    else:
        all_installations = None

    installations = request.user.installation_set.all()
    return render(request, 'installations.html', {'installations': installations, 'all_installations': all_installations})
