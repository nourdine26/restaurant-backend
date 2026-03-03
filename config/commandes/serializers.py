from rest_framework import serializers
from .models import Table, Commande, LigneCommande

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'numero', 'capacite', 'disponible']

class LigneCommandeSerializer(serializers.ModelSerializer):
    plat_nom = serializers.ReadOnlyField(source='plat.nom')
    
    class Meta:
        model = LigneCommande
        fields = ['id', 'plat', 'plat_nom', 'quantite', 'prix_unitaire', 'notes', 'sous_total']

class CommandeSerializer(serializers.ModelSerializer):
    lignes = LigneCommandeSerializer(many=True, read_only=True)
    table_numero = serializers.ReadOnlyField(source='table.numero')
    
    class Meta:
        model = Commande
        fields = ['id', 'table', 'table_numero', 'client_nom', 'statut', 'type_commande', 
                  'date_creation', 'total', 'notes', 'lignes']