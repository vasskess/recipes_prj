from django import forms
from django.forms import ModelForm

from recipes_prj.recipes.models import Recipe, Ingredient


class RecipeCreateForm(ModelForm):
    INGREDIENTS_MAX_LEN = 255
    ingredients = forms.CharField(
        max_length=INGREDIENTS_MAX_LEN,
    )

    class Meta:
        model = Recipe
        fields = ["title", "photo", "description", "time_for_prepare", "likely_cost"]


class RecipeEditForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "photo",
            "description",
            "time_for_prepare",
            "likely_cost",
        ]
