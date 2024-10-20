from django.db import models
from django.contrib.auth.models import User
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    steps = models.TextField()
    cuisine = models.CharField(max_length=100)
    nutritional_info = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
