from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'ingredients', 'description')

admin.site.register(Recipe, RecipeAdmin)