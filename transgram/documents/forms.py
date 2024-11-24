from django import forms

from transgram.documents.models import Document


class DocumentBaseForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['reference', 'invoice', 'cmr', 'additional_document']


class DocumentCreateForm(DocumentBaseForm):
    pass


class DocumentUpdateForm(DocumentBaseForm):
    pass


class DocumentDetailsForm(DocumentBaseForm):
    pass


class DocumentDeleteForm(DocumentBaseForm):
    pass
