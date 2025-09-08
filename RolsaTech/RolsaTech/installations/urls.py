from django.urls import path
from . import views

urlpatterns = [
    path('create-installation/', views.create_installation, name='create_installation'),
    path('edit-installation/<installation_id>/', views.edit_installation, name='edit_installation'),
    path('delete-installation/<installation_id>/', views.delete_installation, name='delete_installation'),
]
