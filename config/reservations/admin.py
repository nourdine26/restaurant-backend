from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['client_nom', 'table', 'date', 'heure', 'nombre_personnes', 'statut']
    list_filter = ['statut', 'date']
    search_fields = ['client_nom', 'client_telephone', 'client_email']
    date_hierarchy = 'date'