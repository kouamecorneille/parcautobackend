from django.db import models


class Marque(models.Model):
    libelle = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    
    
class Vehicule(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    annee_fabrication = models.IntegerField()
    vin = models.CharField(max_length=17, unique=True)
    type_carburant = models.CharField(max_length=50)
    
    numero_plaque = models.CharField(max_length=15, unique=True)
    statut = models.CharField(max_length=20)


class Conducteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numero_permis = models.CharField(max_length=20, unique=True)
    date_expiration_permis = models.DateField()
    numero_telephone = models.CharField(max_length=15)
    adresse_email = models.EmailField(unique=True)

class Entretien(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    type_entretien = models.CharField(max_length=100)
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    date_entretien = models.DateField()
    details_entretien = models.TextField()

class Reservation(models.Model):
    conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()

class Kilometrage(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_record = models.DateField()
    kilometrage = models.DecimalField(max_digits=10, decimal_places=2)

class Assurance(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    compagnie_assurance = models.CharField(max_length=100)
    numero_police = models.CharField(max_length=50, unique=True)
    date_debut_assurance = models.DateField()
    date_fin_assurance = models.DateField()

class Depense(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    type_depense = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_depense = models.DateField()

class Alerte(models.Model):
    type_alerte = models.CharField(max_length=100)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_alerte = models.DateField()
    details_alerte = models.TextField()

class Localisation(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date_localisation = models.DateTimeField()

class Document(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    type_document = models.CharField(max_length=100)
    chemin_fichier = models.FileField(upload_to='documents/')

class HistoriqueUtilisation(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
    date_utilisation = models.DateField()
    kilometrage_parcouru = models.DecimalField(max_digits=10, decimal_places=2)
