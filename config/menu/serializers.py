from rest_framework import serializers
from .models import Categorie, Plat

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nom', 'description']

class PlatSerializer(serializers.ModelSerializer):
    categorie_nom = serializers.ReadOnlyField(source='categorie.nom')
    
    class Meta:
        model = Plat
        fields = ['id', 'nom', 'description', 'prix', 'categorie', 'categorie_nom', 'disponible', 'image']