import tkinter as tk

# função chamada quando o botão "Enviar" é clicado
def enviar():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    print("Nome: ", nome)
    print("Idade: ", idade)

# criação da janela principal
janela = tk.Tk()

# criação dos rótulos e entradas de texto
rotulo_nome = tk.Label(janela, text="Qual o seu nome:")
entrada_nome = tk.Entry(janela)

rotulo_idade = tk.Label(janela, text="Qual sua idade:")
entrada_idade = tk.Entry(janela)

# criação do botão de envio
botao_enviar = tk.Button(janela, text="Enviar", command=enviar)

# posicionamento dos componentes na janela
rotulo_nome.grid(row=0, column=0, padx=10, pady=10)
entrada_nome.grid(row=0, column=1, padx=10, pady=10)

rotulo_idade.grid(row=1, column=0, padx=10, pady=10)
entrada_idade.grid(row=1, column=1, padx=10, pady=10)

botao_enviar.grid(row=2, column=1, padx=10, pady=10)

# exibição da janela
janela.mainloop()