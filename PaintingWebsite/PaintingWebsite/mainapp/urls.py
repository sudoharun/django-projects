from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create-booking', views.createBooking, name='create-booking'),
    path('manage-bookings', views.manageBookings, name='manage-bookings'),
    path('edit-booking/<model_id>', views.editBooking, name='edit-booking'),
    path('delete-booking/<model_id>', views.deleteBooking, name='delete-booking'),
    path('log-in', views.logIn, name='log-in'),
    path('log-out', views.logOut, name='log-out'),
]