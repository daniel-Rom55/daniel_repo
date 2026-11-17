
import tkinter as tk
from tkinter import filedialog, messagebox

ventana = tk.Tk()
ventana.title("Mi editor de texto")
ventana.geometry("600x400")

# Cuadro para escribir y mostrar texto
texto = tk.Text(ventana, wrap="word")
texto.pack(expand=True, fill="both")


def abrir_archivo():
    ruta = filedialog.askopenfilename(
        filetypes=[("Archivos de texto", "*.txt")]
    )

    if not ruta:
        return

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        texto.delete("1.0", tk.END)
        texto.insert("1.0", contenido)

    except OSError as error:
        messagebox.showerror("Error", str(error))


def guardar_archivo():
    ruta = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt")]
    )

    if not ruta:
        return

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            contenido = texto.get("1.0", "end-1c")
            archivo.write(contenido)

        messagebox.showinfo("Guardado", "Archivo guardado correctamente")

    except OSError as error:
        messagebox.showerror("Error", str(error))


# Crear menú
barra = tk.Menu(ventana)
menu_archivo = tk.Menu(barra, tearoff=0)

menu_archivo.add_command(
    label="Abrir", command=abrir_archivo
)
menu_archivo.add_command(
    label="Guardar", command=guardar_archivo
)
menu_archivo.add_separator()
menu_archivo.add_command(
    label="Salir", command=ventana.destroy
)

barra.add_cascade(label="Archivo", menu=menu_archivo)
ventana.config(menu=barra)

ventana.mainloop()
