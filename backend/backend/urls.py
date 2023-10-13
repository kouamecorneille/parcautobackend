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

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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


schema_view = get_schema_view(
    openapi.Info(
      title="API DE GESTION DE PARC AUTOMOBILE",
      default_version='v1',
      description="Application permettant de gerer un parc automobile",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(name="Kouame corneille",email="christkouame153@gmail.com"),
      license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/token/', CustomAuthToken.as_view(), name='token_obtain_pair'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
