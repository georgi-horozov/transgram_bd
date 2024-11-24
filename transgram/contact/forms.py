from django import forms

from transgram.contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'message')

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your e-mail address...'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number...'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message...'}),
        }