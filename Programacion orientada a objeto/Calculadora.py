import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora Sencilla")
ventana.geometry("300x250")

tk.Label(ventana, text="Número 1:", font=("Arial", 12)).pack()
entrada1 = tk.Entry(ventana, font=("Arial", 12))
entrada1.pack(pady=5)

tk.Label(ventana, text="Número 2:", font=("Arial", 12)).pack()
entrada2 = tk.Entry(ventana, font=("Arial", 12))
entrada2.pack(pady=5)

resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 14))
resultado.pack(pady=15)

def sumar():
    try:
        num1 = int(entrada1.get())
        num2 = int(entrada2.get())
        res = num1 + num2
        resultado.config(text=f"Resultado: {res}")
    except ValueError:
        resultado.config(text="Error: Ingresa números")

boton = tk.Button(ventana, text="Sumar", font=("Arial", 12), command=sumar)
boton.pack(pady=10)

ventana.mainloop()
