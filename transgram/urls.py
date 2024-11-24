from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transgram.web.urls')),
    path('accounts/', include('transgram.accounts.urls')),
    path('documents/', include('transgram.documents.urls')),
    path('contact/', include('transgram.contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
