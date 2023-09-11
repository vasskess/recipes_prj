from django.urls import path, include

from recipes_prj.accounts.views import (
    AppUserCreate,
    AppUserLogin,
    AppUserLogout,
    AppUserDetails,
    AppUserEdit,
    AppUserDelete,
)

urlpatterns = [
    path("register/", AppUserCreate.as_view(), name="register"),
    path("login/", AppUserLogin.as_view(), name="login"),
    path("logout/", AppUserLogout.as_view(), name="logout"),
    path(
        "<str:pk>/",
        include(
            [
                path("profile/", AppUserDetails.as_view(), name="profile-details"),
                path("edit/", AppUserEdit.as_view(), name="profile-update"),
                path("delete/", AppUserDelete.as_view(), name="profile-delete"),
            ]
        ),
    ),
]
