from django.db import models
from django.contrib.auth.models import AbstractUser

#role des utilisateur ( ex: admin, client, manager)
class Role(models.Model):
    libelle_role = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.libelle_role


#models user de mon app
class CustomUser(AbstractUser):
    adresse = models.CharField(max_length=100)
    numero_telephone = models.CharField(max_length=15)
    #groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    #user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True, max_length=10)
    
    piece_identite = models.FileField(upload_to="piece_identies", null=True, blank=True,)
    
    
    def __str__(self):
        return self.username