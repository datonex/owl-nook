from django import forms
from django.contrib.auth.forms import UserCreationForm
from owlnookuser.models import OwlNookUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60,
        help_text="Required. Add a valid email address",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password1 = forms.CharField(
        help_text="""
                    <ul class="list-group text-start bg-transparent text-white">
                        <li class="list-group-item bg-transparent text-white">password can't be too similar to your other 
                        personal information.</li>
                        <li class="list-group-item bg-transparent text-white">password must contain at least 8 characters.
                        </li>
                        <li class="list-group-item bg-transparent text-white">password can't be a commonly used password.</li>
                        <li class="list-group-item bg-transparent text-white">password can't be entirely numeric.</li>
                    </ul>
                    """,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    password2 = forms.CharField(
        help_text="Type your password again",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = OwlNookUser
        fields = ("email", "username", "password1", "password2")


class EditUserForm(forms.ModelForm):
    class Meta:
        model = OwlNookUser
        fields = ("email", "password", "username", "is_active", "is_admin")
