from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup', views.signuppage, name='signup'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutview, name='logout'),
    path('adminview', views.adminview, name='adminview'),
    path('user_bookings', views.user_bookings, name='user_bookings'),
    path('create_booking', views.create_booking, name='create_booking'),
    path('edit_booking/<int:booking_id>', views.edit_booking, name='edit_booking'),
    path('delete_booking/<int:booking_id>', views.delete_booking, name='delete_booking'),
    path('create_attraction', views.create_attraction, name='create_attraction'),
    path('edit_attraction/<int:attraction_id>', views.edit_attraction, name='edit_attraction'),
    path('delete_attraction/<int:attraction_id>', views.delete_attraction, name='delete_attraction'),
    path('delete_user/<int:user_id>', views.delete_user, name='delete_user'),
]
