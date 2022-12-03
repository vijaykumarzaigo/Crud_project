import os

from django.core.exceptions import ValidationError


def validate_image_pdf_docx_doc_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extension = ['.pdf']
    if ext.lower() not in valid_extension:
        raise ValidationError('Unsupported file extension. Only PDF file allowed')
