from django.urls import path
from . import views

urlpatterns = [
    path('create-consultation/', views.create_consultation, name='create_consultation'),
    path('edit-consultation/<consultation_id>/', views.edit_consultation, name='edit_consultation'),
    path('delete-consultation/<consultation_id>/', views.delete_consultation, name='delete_consultation'),
]
