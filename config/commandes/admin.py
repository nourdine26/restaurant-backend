from django.contrib import admin
from .models import Table, Commande, LigneCommande

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['numero', 'capacite', 'disponible']
    list_filter = ['disponible']
    list_editable = ['disponible']

class LigneCommandeInline(admin.TabularInline):
    model = LigneCommande
    extra = 1

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_nom', 'table', 'statut', 'type_commande', 'total', 'date_creation']
    list_filter = ['statut', 'type_commande', 'date_creation']
    search_fields = ['id', 'client_nom']
    inlines = [LigneCommandeInline]
    readonly_fields = ['date_creation', 'date_modification']