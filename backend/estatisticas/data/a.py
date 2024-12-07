import pandas as pd

def salvar_dados_filtrados(input_csv, output_csv):
    # Ler o arquivo CSV
    df = pd.read_csv(input_csv)

    # Filtrar as colunas necessárias
    df_filtrado = df[['Estado', 'Municipio', 'RiscoFogo', 'FRP']]

    # Salvar o novo arquivo CSV com as colunas filtradas
    df_filtrado.to_csv(output_csv, index=False)

# Chamar a função passando o caminho do arquivo original e o caminho do arquivo de saída
input_csv = 'dados.csv'  # Caminho do arquivo original
output_csv = 'dados_filtrados.csv'  # Caminho do novo arquivo

salvar_dados_filtrados(input_csv, output_csv)

df = pd.read_csv('dados_filtrados.csv')
print(df)