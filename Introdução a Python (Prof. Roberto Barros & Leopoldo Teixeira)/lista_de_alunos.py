import random

class ListaAlunos:
    def __init__(self, alunos):
        self.alunos = alunos
        self.lista_de_alunos = {}
    
    def mapear_alunos(self, lista_de_alunos):
        for i, alunos in enumerate(self.alunos):
            self.lista_de_alunos[i+1] = alunos
        
        return lista_de_alunos
        


lista_de_alunos = ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Beatriz', 'Arlindo', 'Higor']

lista = ListaAlunos(lista_de_alunos)
alunos_em_lista = lista.mapear_alunos(lista_de_alunos)

print (f'A lista de alunos é {alunos_em_lista}')


#lista = ListaAlunos(alunos)

#aluno_aleatorio = lista.escolher_aluno_aleatorio()

#print(f"O aluno escolhido aleatoriamente foi: {aluno_aleatorio}")
