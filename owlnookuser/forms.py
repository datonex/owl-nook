from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import OwlNookUser


class RegistrationForm(UserCreationForm):

    # https://www.chromium.org/developers/design-documents/form-styles-that-chromium-understands
    # https://stackoverflow.com/questions/36905060/how-can-i-change-the-modelform-label-and-give-it-a-custom-name
    email = forms.EmailField(
        max_length=60,
        help_text="Required. Add a valid email address",
        widget=forms.EmailInput(
            attrs={"autocomplete": "username", "class": "form-control"}
        ),
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password1 = forms.CharField(
        label="Password",
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
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        help_text="Type your password again",
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}
        ),
    )

    class Meta:
        model = OwlNookUser
        fields = ("email", "username", "password1", "password2")


class LoginForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=60,
        widget=forms.EmailInput(
            attrs={"autocomplete": "username", "class": "form-control"}
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "class": "form-control"}
        ),
    )

    class Meta:
        model = OwlNookUser
        fields = ("email", "password")

    def clean(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")


class EditUserForm(forms.ModelForm):
    class Meta:
        model = OwlNookUser
        fields = ("email", "password", "username", "is_active", "is_admin")
