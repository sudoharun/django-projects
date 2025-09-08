from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('my-account/', views.edit_account, name='edit_account'),
    path('my-account/change-password', views.change_password, name='change_password'),
    path('my-account/delete-account', views.delete_account, name='delete_account'),
    path('my-account/delete-account-confirmed', views.account_deletion_confirmed, name='account_deletion_confirmed'),
    path('my-account/my-consultations', views.consultations, name='user_consultations'),
    path('my-account/my-installations', views.installations, name='user_installations'),
]
