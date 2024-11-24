from django.urls import path

from transgram.documents.views import DocumentCreateView, DocumentsHistoryView

urlpatterns = (
    path('create/', DocumentCreateView.as_view(), name='create_document'),
    path('documents_history/', DocumentsHistoryView.as_view(), name='documents_history'),
)