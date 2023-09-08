from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication

class VehiculeViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer

class ConducteurViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Conducteur.objects.all()
    serializer_class = ConducteurSerializer

class EntretienViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Entretien.objects.all()
    serializer_class = EntretienSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class KilometrageViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Kilometrage.objects.all()
    serializer_class = KilometrageSerializer

class AssuranceViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Assurance.objects.all()
    serializer_class = AssuranceSerializer

class DepenseViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Depense.objects.all()
    serializer_class = DepenseSerializer

class AlerteViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Alerte.objects.all()
    serializer_class = AlerteSerializer

class LocalisationViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class HistoriqueUtilisationViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = HistoriqueUtilisation.objects.all()
    serializer_class = HistoriqueUtilisationSerializer

