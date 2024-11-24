from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from transgram.documents.forms import DocumentCreateForm
from transgram.documents.models import Document


UserModel = get_user_model()


class DocumentCreateView(views.CreateView):
    model = Document
    form_class = DocumentCreateForm
    template_name = "documents/upload_document.html"
    success_url = reverse_lazy("index")

    # def form_valid(self, form):
    #     invoice = self.request.FILES.get('invoice')
    #     cmr = self.request.FILES.get('cmr')
    #     additional_document = self.request.FILES.get('additional_document')
    #
    #     if invoice:
    #         form.instance.invoice = invoice
    #
    #     if cmr:
    #         form.instance.cmr = cmr
    #
    #     if additional_document:
    #         form.instance.additional_document = additional_document
    #     form.instance.user = self.request.user
    #
    #     return super().form_valid(form)

    def form_valid(self, form):
        if form.is_valid():
            print("Form is valid!")
        else:
            print("Form is invalid!")
        form.instance.user = self.request.user
        return super().form_valid(form)


class DocumentsHistoryView(LoginRequiredMixin, views.ListView):
    model = Document
    template_name = 'documents/documents_history.html'
    context_object_name = 'documents'

    def get_queryset(self):
        return Document.objects.filter(user = self.request.user)



