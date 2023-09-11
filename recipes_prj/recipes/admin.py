from django.contrib import admin

from recipes_prj.recipes.models import Recipe, Ingredient

admin.site.register(Recipe)
admin.site.register(Ingredient)
