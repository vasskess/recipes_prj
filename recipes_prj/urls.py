from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        include("recipes_prj.recipes.urls"),
    ),
    path(
        "users/",
        include("recipes_prj.accounts.urls"),
    ),
]
