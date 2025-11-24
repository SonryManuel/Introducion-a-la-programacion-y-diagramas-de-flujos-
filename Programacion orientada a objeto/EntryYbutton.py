import tkinter as tk

ventana = tk.Tk()
ventana.title("Mostrar texto")
ventana.geometry("350x200")

entrada = tk.Entry(ventana, font = ("Arial",12))
entrada.pack(pady=10)

resultado = tk.Label(ventana, text = "", font =("Arial", 14))
resultado.pack(pady = 10)

def mostrar_texto():
    texto = entrada.get()
    resultado.config(text = texto)

boton = tk.Button(ventana,text = "Mostrar texto", command = mostrar_texto)
boton.pack(pady = 10)
ventana.mainloop()