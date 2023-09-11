from django.urls import path, include

from recipes_prj.recipes.views import (
    HomePageView,
    RecipesCreate,
    RecipeDetails,
    RecipeEdit,
    RecipeDelete,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="recipes-list"),
    path("create/", RecipesCreate.as_view(), name="recipes-create"),
    path(
        "<str:pk>/",
        include(
            [
                path("detail/", RecipeDetails.as_view(), name="recipe-details"),
                path("edit/", RecipeEdit.as_view(), name="recipe-update"),
                path("delete/", RecipeDelete.as_view(), name="recipe-delete"),
            ]
        ),
    ),
]
