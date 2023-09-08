from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
#     # Vos autres champs
#     adresse = models.CharField(max_length=100)
#     numero_telephone = models.CharField(max_length=15)

#     # Ajoutez ces lignes avec les related_name personnalisés
#     groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
#     user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')
#     def __str__(self):
#         return self.username