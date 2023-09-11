from django.contrib.auth import admin as auth_admin
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class AppUserAdmin(auth_admin.UserAdmin):
    list_display = (
        "email",
        "is_staff",
        "is_superuser",
        "date_joined",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "date_joined",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "groups", "is_superuser")},
        ),
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
    ordering = ("-is_superuser",)
    readonly_fields = ("date_joined",)
