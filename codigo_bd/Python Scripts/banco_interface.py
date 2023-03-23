from mysql.connector import Error
import mysql.connector as MC
from tkinter import *
import tkinter as tk

janela = tk.Tk()
janela.geometry("500x1000")
janela.title('CInUFPE')
janela.resizable(0, 0)

try:
    connect = MC.connect(
    host="localhost",
    user="root",
    passwd="Softex2023",
    database="estoque")
    
    print("MySQL Database connection successful")
except Error as err:
    print("Error: {}".format(err))

while True:
    cursor = connect.cursor()

    # FUNÇÃO CHAMADA AO APERTAR BOTÃO DE OK APÓS ESCOLHA DA OPÇÃO
    def ok():
        texto_saida.config(text=f"funcionando...")
        texto_saida.pack(side="top", padx=5, pady=10)

        a = entrada.get()

        if a == "1": #CADASTRAR FUNCIONARIOS
            etiqueta_nome = tk.Label(janela, text="Digite o nome do funcionário:")
            etiqueta_nome.pack()
            entrada_nome = tk.Entry(janela)
            entrada_nome.pack()

            etiqueta_numero = tk.Label(janela, text="Digite o id do funcionário:")
            etiqueta_numero.pack()
            entrada_numero = tk.Entry(janela)
            entrada_numero.pack()

            etiqueta_cargo = tk.Label(janela, text="Digite o cargo do funcionário:")
            etiqueta_cargo.pack()
            entrada_cargo = tk.Entry(janela)
            entrada_cargo.pack()

            nome = str(entrada_nome)
            numero = str(entrada_numero)
            cargo = str(entrada_cargo)

            botao_ok = tk.Button(janela, text="OK", command=ok) # Chamando função
            botao_ok.pack(side="top", padx=10, pady=10) # posicionamento na tela

            # nome = input("Digite o nome do funcionario: ")
            # numero = input("Digite o id do funcionario: ")
            # cargo = input("Digite o cargo do funcionario: ")
            query_func = """ INSERT INTO funcionarios(id_func, nome_func, cargo )
                                    VALUES('""" + numero + """','""" + nome + """','""" + cargo + """'); """
            cursor.execute(query_func)


    # EXIBIÇÃO DE TEXTO NA TELA
    opcoes_na_tela = tk.Label(janela, text= """1 - cadastrar funcionario
                2 - cadastrar itens
                3 - pesquisar funcionario
                4 - pesquisar itens
                5 - mostrar funcionarios cadastrados
                6 - mostrar itens cadastrados
                7 - atualizar funcionario
                8 - atualizar item
                9 - realizar emprestimos
                10 - realizar devolucoes
                11 - excluir funcionario
                12 - excluir item""")

    opcoes_na_tela.pack(side="top", padx=10, pady=10) # posicionamento na tela



    # a É A VARIÁVEL DE ENTRADA
    entrada = tk.Entry(janela)
    entrada.pack()


    # BOTÃO DE OK
    botao_ok = tk.Button(janela, text="OK", command=ok) # Chamando função
    botao_ok.pack(side="top", padx=10, pady=10) # posicionamento na tela


    # EXIBIÇÃO DO TEXTO DE SAÍDA
    texto_saida = tk.Label(janela)
    texto_saida.pack()


    # MANTER A JANELA EM EXECUÇÃO
    janela.mainloop()
    connect.commit()
    cursor.close()