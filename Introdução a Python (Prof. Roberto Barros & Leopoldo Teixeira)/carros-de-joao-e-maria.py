lista_ano = []
lista_velocidade = []
cont = 0
cont_aux = 0
velocidade_media = 0

adicionar = True
leitura = 'S'

while (adicionar):
    
    if (leitura == 'N'):
            adicionar = False
    
    leitura = input()
    leitura.upper()
    if (leitura == 'S'):
        ano = int(input())
        velocidade = float(input())
        cont_aux += 1

        lista_ano.append(ano)
        lista_velocidade.append(velocidade)
        

print (max(lista_velocidade))
print (max(lista_ano))

