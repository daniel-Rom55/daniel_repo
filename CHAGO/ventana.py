import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("300x150")

# Crear etiqueta con el texto
mensaje = tk.Label(
    ventana,
    text="¿por que el pais necesita ingenieros de software?",
    font=("Arial", 16, "bold"),
    fg="red"   # color rojo
)
mensaje.pack(expand=True)

# Ejecutar la ventana
ventana.mainloop()