import tkinter as tk

# Criar a janela
janela = tk.Tk()
janela.title("Gerenciamento")
janela.geometry('800x400')

# Criar os rótulos
nome_label = tk.Label(janela, text="Nome:")
id_label = tk.Label(janela, text="ID:")
cargo_label = tk.Label(janela, text="Cargo:")

# Posicionar os rótulos na janela
nome_label.grid(row=0, column=0)
id_label.grid(row=1, column=0)
cargo_label.grid(row=2, column=0)

# Criar as variáveis para armazenar as informações do funcionário
nome_var = tk.StringVar()
id_var = tk.StringVar()
cargo_var = tk.StringVar()

# Criar as caixas de entrada para o nome, ID e cargo
nome_entry = tk.Entry(janela, textvariable=nome_var)
id_entry = tk.Entry(janela, textvariable=id_var)
cargo_entry = tk.Entry(janela, textvariable=cargo_var)

# Posicionar as caixas de entrada na janela
nome_entry.grid(row=0, column=1)
id_entry.grid(row=1, column=1)
cargo_entry.grid(row=2, column=1)

# Criar uma função para exibir as informações do funcionário
def exibir_informacoes():
    nome = nome_var.get()
    id = id_var.get()
    cargo = cargo_var.get()
    #print(f"Nome: {nome}\nID: {id}\nCargo: {cargo}")
    texto_saida.config(text=f"O funcionário é {nome} e possui o cargo de {cargo} e seu ID é {id}.")

# Criar um botão para exibir as informações do funcionário
exibir_button = tk.Button(janela, text="Exibir", command=exibir_informacoes)
exibir_button.grid(row=3, column=0, columnspan=2)


# Formatando texto de saída
texto_saida = tk.Label(janela)
texto_saida.grid()

# Iniciar a janela
janela.mainloop()