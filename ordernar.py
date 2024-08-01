import pandas as pd
import os
from unidecode import unidecode

# Caminho para a pasta contendo as planilhas
caminho_pasta = 'dados'
pasta_dados = ''
file_path = os.path.join(pasta_dados, 'planilha_final.xlsx')

# Inicializa uma lista para armazenar todos os DataFrames
todos_dfs = []

# Percorre todos os arquivos na pasta
for arquivo in os.listdir(caminho_pasta):
    if arquivo.endswith('.xlsx'):
        # Lê cada planilha Excel
        df = pd.read_excel(os.path.join(caminho_pasta, arquivo))
        
        todos_dfs.append(df)

# Concatena todos os DataFrames em um único DataFrame
df_final = pd.concat(todos_dfs, ignore_index=True)

# Escreve o DataFrame concatenado na aba única
df_final.to_excel(file_path, sheet_name='dados_combinados', index=False)

print(f'Dados combinados foram salvos em {file_path}')
