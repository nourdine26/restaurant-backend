from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    table_numero = serializers.ReadOnlyField(source='table.numero')
    
    class Meta:
        model = Reservation
        fields = ['id', 'client_nom', 'client_telephone', 'client_email', 
                  'table', 'table_numero', 'date', 'heure', 'nombre_personnes', 
                  'statut', 'demandes_speciales', 'date_creation']