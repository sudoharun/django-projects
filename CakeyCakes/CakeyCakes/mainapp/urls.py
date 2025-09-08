from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('moreDetails/<app_name>/<parent_model>/<model_id>', views.moreDetails, name='more-details'),
    path('logIn', views.logIn, name='log-in'),
    path('logOut', views.logOut, name='log-out'),
    path('signUp', views.signUp, name='sign-up'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('changePassword/<user_id>', views.changePassword, name='change-password'),
    path('editModel/<parent_model>/<model_id>', views.editModel, name='edit-model'),
    path('createModel/<model_name>', views.createModel, name='create-model'),
    path('deleteModel/<parent_model>/<model_id>', views.deleteModel, name='delete-model'),
]
