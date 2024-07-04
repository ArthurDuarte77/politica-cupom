import pandas as pd
import os
from unidecode import unidecode

# Caminho para a pasta contendo as planilhas
caminho_pasta = 'dados'
pasta_dados = ''
file_path = os.path.join(pasta_dados, 'planilha_final.xlsx')

# Inicializa o escritor de Excel
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    # Percorre todos os arquivos na pasta
    for arquivo in os.listdir(caminho_pasta):
        if arquivo.endswith('.xlsx'):
            # Lê cada planilha Excel
            df = pd.read_excel(os.path.join(caminho_pasta, arquivo))
            
            # Gera o nome da aba a partir do nome do arquivo
            nome_aba = os.path.splitext(arquivo)[0]
            nome_aba = unidecode(nome_aba.lower())
            
            # Escreve o DataFrame na aba correspondente
            df.to_excel(writer, sheet_name=nome_aba, index=False)

