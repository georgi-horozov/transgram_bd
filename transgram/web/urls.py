from django.urls import path

from transgram.web.views import index

urlpatterns = (
    path('', index, name='index'),
)