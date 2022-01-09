from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login, authenticate

from .forms import RegistrationForm


class UserRegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = "user/register.html"
    context = {"form": form_class}

    def post(self, request, *args, **kwargs):
        context = dict(registration_form=self.form_class)
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get("email")
                raw_password = form.cleaned_data.get("password1")
                account = authenticate(email=email, password=raw_password)
                login(request, account)
                return redirect("home")
            else:
                context["form"] = form
        else:
            form = RegistrationForm()
            context["form"] = form
        return render(request, "user/register.html", context)
