from rest_framework import viewsets
from .models import Categorie, Plat
from .serializers import CategorieSerializer, PlatSerializer

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class PlatViewSet(viewsets.ModelViewSet):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer
    
    def get_queryset(self):
        queryset = Plat.objects.all()
        categorie_id = self.request.query_params.get('categorie', None)
        disponible = self.request.query_params.get('disponible', None)
        
        if categorie_id:
            queryset = queryset.filter(categorie_id=categorie_id)
        if disponible:
            queryset = queryset.filter(disponible=disponible.lower() == 'true')
        
        return queryset