import tkinter as tk

ventana = tk.Tk()
ventana.title("Dibujar en Canvas")
ventana.geometry("500x400")

canvas = tk.Canvas(ventana, bg="white")
canvas.pack(fill="both", expand=True)

def iniciar_dibujo(event):
    global x, y
    x, y = event.x, event.y

def dibujar(event):
    global x, y
    canvas.create_line(x, y, event.x, event.y)
    x, y = event.x, event.y

canvas.bind("<Button-1>", iniciar_dibujo)
canvas.bind("<B1-Motion>", dibujar)

ventana.mainloop()
