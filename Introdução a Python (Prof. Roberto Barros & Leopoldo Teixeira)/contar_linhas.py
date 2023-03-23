with open('exemplo.txt', 'w') as arquivo:
    arquivo.write("AA\n")
    arquivo.write("BB\n")
    arquivo.write("CC\n")

    arquivo.close()

with open('exemplo.txt', 'a') as arquivo:
    arquivo.write(input('Digite algo: '))

with open('exemplo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    qnt_linhas = len(linhas)
    for i in linhas:
        print (i + '\n')

    print (qnt_linhas)


