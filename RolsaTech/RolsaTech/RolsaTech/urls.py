from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('consultations/', include('consultations.urls')),
    path('installations/', include('installations.urls')),
    path('', include('mainapp.urls'))
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
