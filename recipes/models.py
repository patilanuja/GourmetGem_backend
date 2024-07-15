from django.db import models

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    ingredients = models.TextField()
    image = models.CharField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return self.name
