import os
import shutil

# Função para verificar e mover arquivos XML correspondentes
def mover_arquivos_iguais(lista_ids, pasta_origem, pasta_destino):
    # Cria a pasta destino se não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Itera pela lista de IDs
    for nome_arquivo in os.listdir(pasta_origem):
        if nome_arquivo.endswith(".xml"):
            # Extrai o ID do evento do nome do arquivo
            id_evento_arquivo = nome_arquivo.split('.')[0]
            
            # Verifica se o ID do evento está na lista
            if id_evento_arquivo in lista_ids:
                caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)
                # Move o arquivo para a pasta destino
                shutil.move(caminho_arquivo, os.path.join(pasta_destino, nome_arquivo))
                print(f"Arquivo {nome_arquivo} movido para {pasta_destino}")
            # else:
            #     print(f"Arquivo {nome_arquivo} não encontrado em {pasta_origem}")


lista_ids = [
    #Insira os IDEVENTOS entre aspas e separados por virgula aqui
]

pasta_origem = "C:/Users/itarg/Downloads/s2200"  # Substitua pelo caminho da pasta de origem
pasta_destino = "C:/Users/itarg/Downloads/iguais"  # Substitua pelo caminho da pasta de destino

mover_arquivos_iguais(lista_ids, pasta_origem, pasta_destino)
