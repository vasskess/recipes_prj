from django.db import models
from django.conf import settings
from django.urls import reverse


class Recipe(models.Model):
    TITLE_MAX_LEN = 150
    DESCRIPTION_MAX_LEN = 1500
    PRICE_MAX_DIGIT = 5
    PRICE_DECIMAL_PLACES = 2

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        null=False,
        blank=False,
        verbose_name="Title",
    )
    photo = models.ImageField(upload_to="static/recipes_images", null=True, blank=True)
    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN,
        null=False,
        blank=False,
        verbose_name="Description",
    )
    time_for_prepare = models.PositiveIntegerField()
    likely_cost = models.DecimalField(
        max_digits=PRICE_MAX_DIGIT, decimal_places=PRICE_DECIMAL_PLACES
    )
    ingredients = models.ManyToManyField("Ingredient")

    def get_absolute_url(self):
        return reverse("recipe-details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title[:25]


class Ingredient(models.Model):
    NAME_MAX_LEN = 75

    name = models.CharField(
        max_length=NAME_MAX_LEN, null=False, blank=False, verbose_name="Name"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name[:15]
