from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from recipes_prj.accounts.forms import (
    AppUserCreationForm,
    AppUserLoginForm,
    AppUserEditForm,
)
from recipes_prj.core.account_helpers.get_profile_helper import get_profile_model

User = get_user_model()
Cook = get_profile_model()


class AppUserCreate(CreateView):
    template_name = ""
    form_class = AppUserCreationForm

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "register"
        return context


class AppUserLogin(LoginView):
    template_name = ""
    form_class = AppUserLoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "login"
        return context

    def get_success_url(self):
        return reverse_lazy("profile-details", kwargs={"pk": self.request.user.pk})


class AppUserDetails(DetailView):
    model = User
    template_name = ""


class AppUserEdit(LoginRequiredMixin, UpdateView):
    model = Cook
    form_class = AppUserEditForm
    template_name = ""


class AppUserDelete(LoginRequiredMixin, DeleteView):
    model = User

    def get_success_url(self):
        return reverse_lazy("login")


class AppUserLogout(LoginRequiredMixin, LogoutView):
    def get_success_url(self):
        return reverse_lazy("login")
