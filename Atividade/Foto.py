from PIL import Image
import numpy as np

try:
    imagem_original = Image.open("simple_icon.png").convert("RGB")
    matriz_imagem = np.array(imagem_original)
    
    altura, largura, cores = matriz_imagem.shape
    
    matriz_imagem[:, :, 1] = 0
    matriz_imagem[:, :, 2] = 0
    
    matriz_imagem.tofile("red_channel.bin")
    print("Sucesso: A imagem modificada foi salva no arquivo 'red_channel.bin'.")
    
    dados_lidos = np.fromfile("red_channel.bin", dtype=np.uint8)
    
    matriz_reconstruida = dados_lidos.reshape((altura, largura, cores))
    
    imagem_final = Image.fromarray(matriz_reconstruida)
    imagem_final.show()

except FileNotFoundError:
    print("Erro: A imagem 'foto.jpg' não foi encontrada. Coloque uma foto com esse nome na pasta.")