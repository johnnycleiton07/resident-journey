import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Texto 1")
label1.pack(side="top", padx=10, pady=10)

label2 = tk.Label(root, text="Texto 2")
label2.pack(side="top", padx=10, pady=10)

label3 = tk.Label(root, text="Texto 3")
label3.pack(side="top", padx=10, pady=10)

label4 = tk.Label(root, text="Texto 4")
label4.pack(side="top", padx=10, pady=10)

root.mainloop()


# import tkinter as tk

# root = tk.Tk()

# test = tk.Label(root, text="Red", bg="red", fg="white")
# test.pack(side=tk.BOTTOM)
# test = tk.Label(root, text="Green", bg="green", fg="white")
# test.pack(side=tk.BOTTOM)
# test = tk.Label(root, text="Purple", bg="purple", fg="white")
# test.pack(side=tk.BOTTOM)

# tk.mainloop()

# import tkinter as tk

# root = tk.Tk()

# test = tk.Label(root, text="red", bg="red", fg="white")
# test.pack(padx=5, pady=15, side=tk.LEFT)
# test = tk.Label(root, text="green", bg="green", fg="white")
# test.pack(padx=5, pady=20, side=tk.LEFT)
# test = tk.Label(root, text="purple", bg="purple", fg="white")
# test.pack(padx=5, pady=20, side=tk.LEFT)

# root.mainloop()

# import tkinter as tk

# root = tk.Tk()

# label = tk.Label(root, text="Olá, Mundo!")
# label.pack(side="left", padx=10, pady=10)

# button = tk.Button(root, text="Clique aqui!")
# button.pack(side="left", padx=10, pady=10)

# root.mainloop()

# import tkinter as tk

# root = tk.Tk()

# # Cria um widget Text
# text_widget = tk.Text(root, width=40, height=10)

# # Insere o texto formatado à esquerda
# text_widget.insert(tk.END, "Este texto será formatado à esquerda\naaaa", "left")

# # Define o alinhamento do texto para a esquerda
# text_widget.tag_configure("left", justify="left")

# # Exibe o widget Text
# text_widget.pack()

# root.mainloop()
