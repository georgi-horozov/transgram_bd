from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from transgram.accounts.forms import TransgramUserCreationForm, TransgramUserChangeForm
from transgram.accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    model = UserModel
    add_form = TransgramUserCreationForm
    form = TransgramUserChangeForm

    list_display = ('id', 'email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    list_filter = ('id',)
    ordering = ('id',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('company_name', 'vat', 'address', 'phone_number', 'profile_photo')
    search_fields = ('vat',)
    list_filter = ('vat',)
    ordering = ('company_name',)

