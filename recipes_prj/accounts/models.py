from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from django.conf import settings
from django.urls import reverse

from recipes_prj.accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_ERROR = "User with that email already exists."

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        verbose_name="Email",
        error_messages={"unique": USERNAME_ERROR},
    )
    is_active = models.BooleanField(default=True, verbose_name="Active status")
    is_staff = models.BooleanField(
        default=False, null=False, blank=False, verbose_name="Staff status"
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = "email"
    objects = AppUserManager()

    class Meta:
        ordering = ["email"]

    def get_absolute_url(self):
        return reverse("profile-details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.email.split("@")[0].capitalize()


class CookProfile(models.Model):
    FIRST_NAME_MIN_LEN = 3
    FIRST_NAME_MAX_LEN = 15
    FIRST_NAME_MIN_LEN_MESSAGE = (
        f"First name must contains at least {FIRST_NAME_MIN_LEN} characters"
    )

    LAST_NAME_MIN_LEN = 3
    LAST_NAME_MAX_LEN = 15
    LAST_NAME_MIN_LEN_MESSAGE = (
        f"Last name must contains at least {FIRST_NAME_MIN_LEN} characters"
    )

    LOCATION_MIN_LEN = 3
    LOCATION_MAX_LEN = 75
    LOCATION_MIN_LEN_MESSAGE = (
        f"Location name must contains at least {FIRST_NAME_MIN_LEN} characters"
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="User email",
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN, FIRST_NAME_MIN_LEN_MESSAGE),
        ),
        null=False,
        blank=False,
        verbose_name="First Name",
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(MinLengthValidator(LAST_NAME_MIN_LEN, LAST_NAME_MIN_LEN_MESSAGE),),
        null=False,
        blank=False,
        verbose_name="Last Name",
    )
    location = models.CharField(
        max_length=LOCATION_MAX_LEN,
        validators=(MinLengthValidator(LOCATION_MIN_LEN, LOCATION_MIN_LEN_MESSAGE),),
        null=False,
        blank=False,
        verbose_name="Location",
    )

    def get_absolute_url(self):
        return reverse("profile-details", kwargs={"pk": self.pk})

    def __str__(self):
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        return self.user.__str__()
