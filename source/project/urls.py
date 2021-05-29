from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gallery.urls', namespace='photo-list')),
    path('', include('accounts.urls', namespace='account')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

