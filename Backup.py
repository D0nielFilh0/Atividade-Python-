import os

arquivo_original = "meu_arquivo.txt"
arquivo_backup = "backup_dados.txt"

if os.path.exists(arquivo_original):
    
    if os.path.exists(arquivo_backup):
        print(f"Aviso: O arquivo '{arquivo_backup}' já existe! Operação cancelada.")
    else:
        try:
            os.rename(arquivo_original, arquivo_backup)
            print(f"Sucesso! Arquivo renomeado para '{arquivo_backup}'.")
        except Exception as erro:
            print(f"Erro ao tentar renomear o arquivo: {erro}")
            
else:
    print(f"Erro: O arquivo '{arquivo_original}' não foi encontrado.")