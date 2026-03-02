from django.db import models
from commandes.models import Table

class Reservation(models.Model):
    STATUTS = [
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('annulee', 'Annulée'),
        ('terminee', 'Terminée'),
    ]
    
    client_nom = models.CharField(max_length=200)
    client_telephone = models.CharField(max_length=20)
    client_email = models.EmailField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reservations')
    date = models.DateField()
    heure = models.TimeField()
    nombre_personnes = models.IntegerField()
    statut = models.CharField(max_length=20, choices=STATUTS, default='en_attente')
    demandes_speciales = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.client_nom} - {self.date} {self.heure}"
    
    class Meta:
        ordering = ['date', 'heure']
        unique_together = ['table', 'date', 'heure']