import tkinter  as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x300")
root.title('CINUFPE')
root.resizable(0, 0)

root.columnconfigure(0, weight=10) 
root.columnconfigure(1, weight=20)


# LEGENDA E ENTRADA DE DADOS
# 1 sticky=tk.W, sticky=tk.E,
username_label = ttk.Label(root, text="Digite o nome do funcionário:")
username_label.grid(column=0, row=0, padx=50, pady=50)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, padx=80, pady=5)


# 2
username_label = ttk.Label(root, text="Digite o cargo do funcionário:")
username_label.grid(column=0, row=1, padx=50, pady=50)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=1, padx=80, pady=5)

# 3
username_label = ttk.Label(root, text="Digite a ID do funcionário:")
username_label.grid(column=0, row=2, padx=50, pady=50)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=2, padx=80, pady=5)


root.mainloop()