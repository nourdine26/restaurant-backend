from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Table, Commande
from .serializers import TableSerializer, CommandeSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all().prefetch_related('lignes__plat')
    serializer_class = CommandeSerializer
    
    @action(detail=True, methods=['post'])
    def changer_statut(self, request, pk=None):
        commande = self.get_object()
        nouveau_statut = request.data.get('statut')
        
        if nouveau_statut in dict(Commande.STATUTS):
            commande.statut = nouveau_statut
            commande.save()
            return Response({'message': 'Statut mis à jour', 'statut': nouveau_statut})
        
        return Response({'erreur': 'Statut invalide'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def aujourd_hui(self, request):
        aujourd_hui = timezone.now().date()
        commandes = self.queryset.filter(date_creation__date=aujourd_hui)
        serializer = self.get_serializer(commandes, many=True)
        return Response(serializer.data)