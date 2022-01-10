from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import RegistrationForm, EditUserForm
from .models import OwlNookUser


class UserAdmin(BaseUserAdmin):
    model = OwlNookUser
    form = EditUserForm
    add_form = RegistrationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("username", "email", "is_admin", "is_active")
    list_filter = ("is_admin", "is_active")
    fieldsets = (
        (
            "Login details",
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "Profile",
            {
                "fields": (
                    "username",
                    "avatar_image",
                    "biography",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_admin", "is_superuser")},
        ),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_admin",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = (
        "email",
        "username",
        "first_name",
        "last_name",
    )
    ordering = ("email",)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(OwlNookUser, UserAdmin)
