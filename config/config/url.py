from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.urls import path

def create_admin(request):
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', '', 'admin123')
        return HttpResponse("✅ Admin créé avec succès !")
    return HttpResponse("✅ Admin existe déjà !")

urlpatterns = [
    path('create-admin/', create_admin),  # Ajoutez cette ligne
    # ... vos autres URLs
]