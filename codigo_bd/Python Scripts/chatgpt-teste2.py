import tkinter as tk

root = tk.Tk()
root.geometry("500x300")
root.title('CINUFPE')
root.resizable(0, 0)

# função para exibir o nome e a idade na janela
def mostrar_dados():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    texto_saida.config(text=f"O funcionário é {nome} e seu ID é {idade}.")


# cria a etiqueta de pergunta e a entrada de texto para o nome
etiqueta_nome = tk.Label(root, text="Digite o nome do funcionário:")
etiqueta_nome.pack()
entrada_nome = tk.Entry(root)
entrada_nome.pack()

# cria a etiqueta de pergunta e a entrada de texto para a idade
etiqueta_idade = tk.Label(root, text="Digite o número ID do funcionário:")
etiqueta_idade.pack()
entrada_idade = tk.Entry(root)
entrada_idade.pack()

# cria o botão de envio
botao_enviar = tk.Button(root, text="Enviar", command=mostrar_dados)
botao_enviar.pack()

# cria a etiqueta de saída
texto_saida = tk.Label(root)
texto_saida.pack()

# inicia a root
root.mainloop()
