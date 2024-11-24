from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.password_validation import validate_password


UserModel = get_user_model()


class TransgramUserCreationForm(auth_forms.UserCreationForm):
    user = None
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter e-mail address...'})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password...'})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password...'})
    )

    def clean_password2(self):
        password2 = super().clean_password2()
        validate_password(password2)
        return password2

    class Meta(auth_forms.UserCreationForm):
        model = UserModel
        fields = ('email',)


class TransgramUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel

