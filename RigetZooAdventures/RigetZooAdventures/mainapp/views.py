from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import BookingForm, SignUpForm, LoginForm, AttractionForm
from .models import Booking, Attraction, User

# Homepages

def adminview(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Not logged in!')
        return redirect('homepage')

    context = {
        'users': User.objects.all(),
        'attractions': Attraction.objects.all(),
        'bookings': Booking.objects.all(),
    }
    return render(request, 'admin_view.html', context)

def homepage(request):
    if request.user.is_superuser:
        return redirect('adminview')

    context = {
        'attractions': Attraction.objects.all(),
    }
    return render(request, 'homepage.html', context)

# Account-related views

def signuppage(request):
    if request.user.is_authenticated:
        messages.error(request, 'Already logged in!')
        return redirect('homepage')

    if request.method == 'GET':
        form = SignUpForm()
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'Successfully signed up!')
            else:
                messages.error(request, 'Fatal error!')
            return redirect('homepage')

    context = {'form': form}
    return render(request, 'signup.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.error(request, 'Already logged in!')
        return redirect('homepage')

    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged in!')
                return redirect('homepage')

    context = {'form': form}
    return render(request, 'login.html', context)

def logoutview(request):
    if request.user is not None:
        logout(request)
        messages.success(request, 'Successfully logged out!')

    return redirect('homepage')

# Booking-related views

def user_bookings(request):
    if not request.user.is_authenticated or request.user.is_superuser:
        return redirect('homepage')

    bookings = Booking.objects.filter(user=request.user)

    context = {'bookings': bookings}
    return render(request, 'user_bookings.html', context)

def create_booking(request):
    if not request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'GET':
        form = BookingForm(user=request.user)
    else:
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created booking!')
            return redirect('user_bookings')

    context = {'form': form}
    return render(request, 'create_booking.html', context)

def edit_booking(request, booking_id: int):
    if request.user.is_superuser:
        booking = get_object_or_404(Booking, id=booking_id)
    else:
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'GET':
        form = BookingForm(instance=booking)
    else:
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('user_bookings')

    context = {'form': form}
    return render(request, 'edit_booking.html', context)

def delete_booking(request, booking_id: int):
    if request.user.is_superuser:
        booking = get_object_or_404(Booking, id=booking_id)
    else:
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    booking.delete()
    messages.success(request, 'Successfully deleted booking.')
    return redirect('user_bookings')

# Attraction-related views

def create_attraction(request):
    if not request.user.is_superuser:
        return redirect('homepage')

    if request.method == 'GET':
        form = AttractionForm()
    else:
        form = AttractionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created attraction!')
            return redirect('adminview')

    context = {'form': form}
    return render(request, 'create_attraction.html', context)

def edit_attraction(request, attraction_id: int):
    attraction = get_object_or_404(Attraction, id=attraction_id)
    if request.method == 'GET':
        form = AttractionForm(instance=attraction)
    else:
        form = AttractionForm(request.POST, instance=attraction)
        if form.is_valid():
            form.save()
            return redirect('adminview')

    context = {'form': form}
    return render(request, 'edit_attraction.html', context)

def delete_attraction(request, attraction_id: int):
    attraction = get_object_or_404(Attraction, id=attraction_id)
    attraction.delete()
    messages.success(request, 'Successfully deleted attraction.')
    return redirect('adminview')

# Other admin-related views

def delete_user(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'Successfully deleted user.')
    return redirect('adminview')
