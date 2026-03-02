from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

class Plat(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='plats')
    disponible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='plats/', blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nom} - {self.prix}€"
    
    class Meta:
        verbose_name = "Plat"
        verbose_name_plural = "Plats"