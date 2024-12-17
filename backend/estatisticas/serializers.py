from rest_framework import serializers
from .models import Queimada
from .models import Municipio
from .models import Sugestao

class QueimadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queimada
        fields = ['municipio', 'risco_fogo', 'frp']

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['estado', 'nome']

class SugestaoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Sugestao
        fields = ['nome', 'email', 'mensagem']
                
