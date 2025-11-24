import tkinter as tk

ventana = tk.Tk()
ventana.title("Lista de Elementos")
ventana.geometry("300x300")

listbox = tk.Listbox(ventana, font=("Arial", 12))
listbox.pack(pady=10)

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

def agregar():
    elemento = entrada.get()
    if elemento.strip() != "":
        listbox.insert(tk.END, elemento)
        entrada.delete(0, tk.END)

boton = tk.Button(ventana, text="Agregar Elemento", font=("Arial", 12), command=agregar)
boton.pack(pady=10)

ventana.mainloop()
