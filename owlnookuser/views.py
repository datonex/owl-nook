from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login, authenticate, logout

from .forms import LoginForm, RegistrationForm


class UserRegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = "user/register.html"

    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == "POST":
            form = self.form_class(request.POST)
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
            form = self.form_class

        return render(request, self.template_name, context)


class UserLoginView(generic.View):
    form_class = LoginForm
    template_name = "user/login.html"

    def get(self, request):
        context = {}
        user = request.user
        if user.is_authenticated:
            return redirect("home")
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                email = request.POST["email"]
                password = request.POST["password"]
                user = authenticate(email=email, password=password)

                if user:
                    login(request, user)
                    return redirect("login")
        else:
            form = self.form_class

        context["login_form"] = form
        return render(request, self.template_name, context)


def logout_view(request):
    logout(request)
    return redirect("home")
