from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication

class VehiculeViewSet(viewsets.ModelViewSet):
  
    """
      is creating summary for VehiculeViewSet
      this class is use to manage a vehicule class (add, get, delete, put, patch)
    """
    authentication_classes = [TokenAuthentication]
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer

class ConducteurViewSet(viewsets.ModelViewSet):
    
    """
      is creating summary for ConducteurViewSet
      this class is use to manage a conducteur class (add, get, delete, put, patch)
    """
    
    authentication_classes = [TokenAuthentication]
    queryset = Conducteur.objects.all()
    serializer_class = ConducteurSerializer

class EntretienViewSet(viewsets.ModelViewSet):
    
    """
      is creating summary for EntretienViewSet
      this class is use to manage a entretien class (add, get, delete, put, patch)
    """
    
    authentication_classes = [TokenAuthentication]
    queryset = Entretien.objects.all()
    serializer_class = EntretienSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    
    """
      is creating summary for ReservationViewSet
      this class is use to manage a reservation class (add, get, delete, put, patch)
    """
    
    authentication_classes = [TokenAuthentication]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class KilometrageViewSet(viewsets.ModelViewSet):
    
    """
      is creating summary for KilometrageViewSet
      this class is use to manage a Kilometrage class (add, get, delete, put, patch)
    """
    authentication_classes = [TokenAuthentication]
    queryset = Kilometrage.objects.all()
    serializer_class = KilometrageSerializer

class AssuranceViewSet(viewsets.ModelViewSet):
    
    """
      is creating summary for AssuranceViewSet
      this class is use to manage a Assurance class (add, get, delete, put, patch)
    """
    
    authentication_classes = [TokenAuthentication]
    queryset = Assurance.objects.all()
    serializer_class = AssuranceSerializer

class DepenseViewSet(viewsets.ModelViewSet):
    
    """
      is creating summary for DepenseViewSet
      this class is use to manage a Depense class (add, get, delete, put, patch)
    """
    
    authentication_classes = [TokenAuthentication]
    queryset = Depense.objects.all()
    serializer_class = DepenseSerializer

class AlerteViewSet(viewsets.ModelViewSet):
    
    """
      is creating summary for AlerteViewSet
      this class is use to manage a Alerte class (add, get, delete, put, patch)
    """
    
    authentication_classes = [TokenAuthentication]
    queryset = Alerte.objects.all()
    serializer_class = AlerteSerializer

class LocalisationViewSet(viewsets.ModelViewSet):
    """
      is creating summary for LocalisationViewSet
      this class is use to manage a Localisation class (add, get, delete, put, patch)
    """
    authentication_classes = [TokenAuthentication]
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    
    """
      is creating summary for Document
      this class is use to manage a Document class (add, get, delete, put, patch)
    """
    
    authentication_classes = [TokenAuthentication]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class HistoriqueUtilisationViewSet(viewsets.ModelViewSet):
    
    """
      is creating summary for HistoriqueUtilisationViewSet
      this class is use to manage a HistoriqueUtilisation class (add, get, delete, put, patch)
    """
    
    authentication_classes = [TokenAuthentication]
    queryset = HistoriqueUtilisation.objects.all()
    serializer_class = HistoriqueUtilisationSerializer

