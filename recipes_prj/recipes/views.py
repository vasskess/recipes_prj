from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from recipes_prj.core.recipes_helpers.recipe_owner_mixin import RecipeOwnerMixin
from recipes_prj.recipes.forms import RecipeCreateForm, RecipeEditForm
from recipes_prj.recipes.models import Recipe, Ingredient


class HomePageView(ListView):
    model = Recipe
    template_name = "recipes/home.html"


class RecipesCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = ""

    def form_valid(self, form):
        form.instance.user = self.request.user
        ingredients = form.cleaned_data.get("ingredients", "")
        ingredient_names = [name.strip() for name in ingredients.split(",")]
        form.save()
        for ingredient_name in ingredient_names:
            if ingredient_name:
                ingredient, created = Ingredient.objects.get_or_create(
                    name=ingredient_name, user=self.request.user
                )
                form.instance.ingredients.add(ingredient)

        return super().form_valid(form)


class RecipeDetails(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = ""
    context_object_name = "recipe"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_ingredients"] = self.object.ingredients.all()
        return context


class RecipeEdit(LoginRequiredMixin, RecipeOwnerMixin, UpdateView):
    model = Recipe
    form_class = RecipeEditForm
    template_name = ""

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.save()
        ingredients_text = self.request.POST.get("ingredients", "")
        ingredient_names = [name.strip() for name in ingredients_text.split(",")]
        form.instance.ingredients.clear()
        for ingredient_name in ingredient_names:
            if ingredient_name:
                ingredient, created = Ingredient.objects.get_or_create(
                    name=ingredient_name, user=self.request.user
                )
                form.instance.ingredients.add(ingredient)

        return super().form_valid(form)


class RecipeDelete(LoginRequiredMixin, RecipeOwnerMixin, DeleteView):
    model = Recipe

    def get_success_url(self):
        return reverse_lazy("recipes-list")
