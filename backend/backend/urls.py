"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from gestion_parc.views import VehiculeViewSet, ConducteurViewSet, EntretienViewSet, ReservationViewSet, KilometrageViewSet, AssuranceViewSet, DepenseViewSet, AlerteViewSet, LocalisationViewSet, DocumentViewSet, HistoriqueUtilisationViewSet
from django.urls import path, include
from account.token import CustomAuthToken
router = DefaultRouter()
router.register(r'vehicules', VehiculeViewSet, basename='vehicule')
router.register(r'conducteurs', ConducteurViewSet, basename='conducteur')
router.register(r'entretiens', EntretienViewSet, basename='entretien')
router.register(r'reservations', ReservationViewSet, basename='reservation')
router.register(r'kilometrages', KilometrageViewSet, basename='kilometrage')
router.register(r'assurances', AssuranceViewSet, basename='assurance')
router.register(r'depenses', DepenseViewSet, basename='depense')
router.register(r'alertes', AlerteViewSet, basename='alerte')
router.register(r'localisations', LocalisationViewSet, basename='localisation')
router.register(r'documents', DocumentViewSet, basename='document')
router.register(r'historiques', HistoriqueUtilisationViewSet, basename='historiqueutilisation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/token/', CustomAuthToken.as_view(), name='token_obtain_pair'),

]
