from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from estatisticas.models import Queimada
from estatisticas.models import Municipio
from estatisticas.serializers import QueimadaSerializer
from estatisticas.serializers import MunicipioSerializer
from rest_framework import status

class QueimadaList(APIView):
    def get(self, request):
        municipio = request.query_params.get('municipio', None)
        
        # Filtra as queimadas por município, caso seja passado como parâmetro
        if municipio:
            queryset = Queimada.objects.filter(municipio__nome=municipio)
        else:
            queryset = Queimada.objects.all()
        
        serializer = QueimadaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MunicipioList(generics.ListCreateAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

