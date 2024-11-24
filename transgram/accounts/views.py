from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, logout, login

from transgram.accounts.forms import TransgramUserCreationForm
from transgram.accounts.models import Profile


class LoginUserView(auth_views.LoginView):
    template_name = "accounts/login_user.html"
    redirect_authenticated_user = True

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your email',
        })
        form.fields['password'].widget.attrs.update({
            'placeholder': 'Enter your password',
        })
        return form


class RegisterUserView(views.CreateView):
    form_class = TransgramUserCreationForm
    template_name = "accounts/register_user.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result

def logout_user(request):
    logout(request)
    return redirect('login_user')


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = "accounts/profile_details.html"


class ProfileUpdateView(views.UpdateView):
    model = Profile
    template_name = "accounts/profile_update.html"
    fields = ("company_name", "vat", "address", "phone_number", "profile_photo")

    def form_valid(self, form):
        profile_photo = self.request.FILES.get("profile_photo")
        if profile_photo:
            form.instance.profile_photo = profile_photo
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("profile_details", kwargs={"pk": self.object.pk})


class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "accounts/profile_delete.html"
    success_url = reverse_lazy('index')