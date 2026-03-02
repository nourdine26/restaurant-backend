from django.db import models
from menu.models import Plat

class Table(models.Model):
    numero = models.IntegerField(unique=True)
    capacite = models.IntegerField()
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Table {self.numero} ({self.capacite} pers.)"

class Commande(models.Model):
    STATUTS = [
        ('en_attente', 'En attente'),
        ('en_preparation', 'En préparation'),
        ('pret', 'Prêt'),
        ('servi', 'Servi'),
        ('paye', 'Payé'),
        ('annule', 'Annulé'),
    ]
    
    TYPES = [
        ('sur_place', 'Sur place'),
        ('emporter', 'À emporter'),
        ('livraison', 'Livraison'),
    ]
    
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    client_nom = models.CharField(max_length=200, blank=True)
    statut = models.CharField(max_length=20, choices=STATUTS, default='en_attente')
    type_commande = models.CharField(max_length=20, choices=TYPES, default='sur_place')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Commande #{self.id} - {self.date_creation.strftime('%d/%m/%Y %H:%M')}"
    
    class Meta:
        ordering = ['-date_creation']

class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='lignes')
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=200, blank=True)
    
    def sous_total(self):
        return self.quantite * self.prix_unitaire
    
    def __str__(self):
        return f"{self.quantite}x {self.plat.nom}"