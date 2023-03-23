with open('exemplo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha)
