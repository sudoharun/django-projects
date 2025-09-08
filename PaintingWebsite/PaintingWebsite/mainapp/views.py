from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Booking
from .forms import BookingForm

# Create your views here.
def homepage(request):
    autheticated = False
    if request.user.is_superuser:
        autheticated = True

    context = {
        "authenticated": autheticated,
    }
    return render(request, 'homepage.html', context)

def logIn(request):
    autheticated = False
    if request.user.is_superuser:
        autheticated = True

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect("homepage")
        else:
            messages.error(request, "The was a problem signing you in.")
    
    context = {
        "authenticated": autheticated,
    }
    return render(request, 'log_in.html', context)

def logOut(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('homepage')

def createBooking(request):
    autheticated = False
    if request.user.is_superuser:
        autheticated = True

    if request.method == "GET":
        form = BookingForm()
    else:
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The booking was created successfully.")
            return redirect("homepage")

    context = {
        "form": form,
        "authenticated": autheticated,
    }
    return render(request, 'create_booking.html', context)

def manageBookings(request):
    autheticated = False
    if request.user.is_superuser:
        autheticated = True

    models = Booking.objects.all()
    context = {
        "bookings": models,
        "authenticated": autheticated,
    }
    return render(request, 'manage_bookings.html', context)

def editBooking(request, model_id):
    autheticated = False
    if request.user.is_superuser:
        autheticated = True

    model = Booking.objects.get(pk=model_id)
    form = BookingForm(request.POST or None, instance=model)
    if form.is_valid():
        form.save()
        messages.success(request, "The booking was successfully edited.")
        return redirect("manage-bookings")

    context = {
        "form": form,
        "authenticated": autheticated,
    }
    return render(request, 'edit_booking.html', context)

def deleteBooking(request, model_id):
    model = Booking.objects.get(pk=model_id)
    model.delete()
    messages.success(request, "The booking was successfully deleted.")
    return redirect("manage-bookings")

