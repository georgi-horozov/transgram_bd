from django.contrib import admin

from transgram.documents.models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    model = Document
    list_display = ['reference', 'invoice', 'cmr', 'additional_document']
    search_fields = ['reference']
    list_filter = ['reference']
    ordering = ['reference']

