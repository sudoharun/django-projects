from django.urls import path
from . import views

urlpatterns = [
    path('create-product/', views.create_product, name='create_product'),
    path('edit-product/<product_id>/', views.edit_product, name='edit_product'),
    path('delete-product/<product_id>/', views.delete_product, name='delete_product')
]
