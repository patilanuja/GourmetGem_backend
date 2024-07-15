from rest_framework import viewsets
from .serializers import RecipeSerializer
from .models import Recipe

# Create your views here.

class RecipeView(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    
