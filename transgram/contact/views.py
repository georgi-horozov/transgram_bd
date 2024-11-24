from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib import messages


from transgram.contact.forms import ContactForm
from transgram.contact.models import Contact

UserModel = get_user_model()


class ContactCreateView(views.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/create_message.html'

    def form_valid(self, form):
        messages.success(self.request, "Your message has been successfully sent!")

        return super().form_valid(form)

    success_url = reverse_lazy('create_message')



