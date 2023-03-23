import tkinter as tk

# Criação da janela principal
root = tk.Tk()
root.title("Cadastro de funcionários")
root.geometry("800x400")

# Criação do rótulo e caixa de texto para o nome
lbl_nome = tk.Label(root, text="Digite o nome do funcionário:")
lbl_nome.grid(row=0, column=0, padx=10, pady=10)

ent_nome = tk.Entry(root)
ent_nome.grid(row=0, column=1, padx=10, pady=10)

# Criação do rótulo e caixa de texto para o cargo
lbl_cargo = tk.Label(root, text="Digite o cargo do funcionário:")
lbl_cargo.grid(row=1, column=0, padx=10, pady=10)

ent_cargo = tk.Entry(root)
ent_cargo.grid(row=1, column=1, padx=10, pady=10)

# Criação do rótulo e caixa de texto para o identificador
lbl_id = tk.Label(root, text="Digite o identificador do funcionário:")
lbl_id.grid(row=2, column=0, padx=10, pady=10)

ent_id = tk.Entry(root)
ent_id.grid(row=2, column=1, padx=10, pady=10)

# Inicia a janela
root.mainloop()