from django.urls import path

from transgram.contact.views import ContactCreateView

urlpatterns = (
    path('create_message/', ContactCreateView.as_view(), name='create_message'),
)