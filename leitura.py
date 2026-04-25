try:
    with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()
        

    palavra = input("Digite a palavra que deseja buscar: ")
    
    texto_minusculo = texto.lower()
    palavra_minuscula = palavra.lower()

    quantidade = texto_minusculo.count(palavra_minuscula)
    
    print(f"\nA palavra '{palavra}' foi encontrada {quantidade} vezes.")
    
except FileNotFoundError:

    print("Erro: O arquivo 'meu_arquivo.txt' não foi encontrado na pasta.")