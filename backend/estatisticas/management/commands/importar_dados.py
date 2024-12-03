import pandas as pd
import os
from django.core.management.base import BaseCommand
from estatisticas.models import Municipio, Queimada
from decimal import Decimal
from datetime import datetime

class Command(BaseCommand):
    help = 'Importa dados de queimadas de um arquivo CSV usando Pandas'

    def handle(self, *args, **kwargs):
        # Caminho do arquivo CSV
        csv_file = os.path.join('estatisticas', 'data', 'dados_filtrados.csv')

        try:
            # Ler o arquivo CSV com pandas
            df = pd.read_csv(csv_file, delimiter=',')  # Ajuste o delimitador conforme necessário

            # Loop sobre as linhas do DataFrame
            for _, row in df.iterrows():
                # Criar ou obter o município
                municipio, created = Municipio.objects.get_or_create(
                    estado=row['Estado'],
                    nome=row['Municipio'],
                )

                # Converter os dados de DiaSemChuva para Decimal, e outros tipos conforme necessário
                risco_fogo = float(row['RiscoFogo']) if row['RiscoFogo'] else 0.0
                frp = float(row['FRP'])


                # Criar o registro de Queimada
                Queimada.objects.create(
                    municipio=municipio,
                    risco_fogo=risco_fogo,
                    frp=frp
                )

            self.stdout.write(self.style.SUCCESS("Dados importados com sucesso!"))
        
        except Exception as e:
            self.stderr.write(f"Erro ao processar o arquivo: {e}")