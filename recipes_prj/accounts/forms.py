from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms import ModelForm

from recipes_prj.core.account_helpers.get_profile_helper import get_profile_model

User = get_user_model()
Cook = get_profile_model()


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (User.USERNAME_FIELD,)


class AppUserLoginForm(AuthenticationForm):
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password")

        return super().clean()


class AppUserEditForm(ModelForm):
    class Meta:
        model = Cook
        exclude = ("user",)
