import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana de Bienvenida")
ventana.geometry("300x150")


mensaje = tk.Label(ventana, text = "Bienvenido maestro ", font=("Arial",14) )
mensaje.pack(pady=20)

ventana.mainloop()