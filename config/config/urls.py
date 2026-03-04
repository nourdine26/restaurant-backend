from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from menu.views import CategorieViewSet, PlatViewSet
from commandes.views import TableViewSet, CommandeViewSet
from reservations.views import ReservationViewSet

def create_admin(request):
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', '', 'admin123')
        return HttpResponse("✅ Admin créé avec succès ! Utilisateur: admin, Mot de passe: admin123")
    return HttpResponse("✅ Admin existe déjà ! Vous pouvez vous connecter avec admin/admin123")
router = DefaultRouter()
router.register(r'categories', CategorieViewSet)
router.register(r'plats', PlatViewSet)
router.register(r'tables', TableViewSet)
router.register(r'commandes', CommandeViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)