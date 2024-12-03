from django.urls import path
from .views import QueimadaList
from .views import MunicipioList

urlpatterns = [
    path('api/queimadas/', QueimadaList.as_view(), name='queimadas-list'),
    path('api/municipios/', MunicipioList.as_view(), name='municipio-list'),
]