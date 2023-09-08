from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Ajoutez des champs supplémentaires si nécessaire
    adresse = models.CharField(max_length=100)
    numero_telephone = models.CharField(max_length=15)

    def __str__(self):
        return self.username
