import tkinter as tk
from tkinter import messagebox
from cmath import sqrt


def calcular_raices():
    try:
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())
    except ValueError:
        messagebox.showerror("Entrada no válida", "Introduce números válidos para a, b y c.")
        return

    if a == 0:
        messagebox.showerror("Ecuación no válida", "El coeficiente a no puede ser cero.")
        return

    discriminante = b ** 2 - 4 * a * c
    x1 = (-b + sqrt(discriminante)) / (2 * a)
    x2 = (-b - sqrt(discriminante)) / (2 * a)
    resultado.config(
        text=(
            f"Discriminante: {discriminante}\n"
            f"x₁ = {x1.real:g}{x1.imag:+g}i\n"
            f"x₂ = {x2.real:g}{x2.imag:+g}i"
        )
    )


def limpiar_campos():
    entrada_a.delete(0, tk.END)
    entrada_b.delete(0, tk.END)
    entrada_c.delete(0, tk.END)
    resultado.config(
        text="Introduce los coeficientes para ver las soluciones."
    )
    entrada_a.focus_set()


def salir_aplicacion():
    ventana.destroy()


FONDO = "#101827"
TARJETA = "#1b2738"
ACENTO = "#38bdf8"
TEXTO = "#f1f5f9"
SECUNDARIO = "#aab8ca"

ventana = tk.Tk()
ventana.title("Fórmula general | Calculadora")
ventana.resizable(False, False)
ventana.configure(bg=FONDO)

menu_bar = tk.Menu(ventana)
menu_opciones = tk.Menu(menu_bar, tearoff=0)
menu_opciones.add_command(label="Limpiar", command=limpiar_campos)
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=salir_aplicacion)
menu_bar.add_cascade(label="Opciones", menu=menu_opciones)
ventana.config(menu=menu_bar)

contenedor = tk.Frame(ventana, bg=FONDO, padx=32, pady=28)
contenedor.pack()

tk.Label(
    contenedor,
    text="MATEMÁTICAS · ÁLGEBRA",
    font=("Arial", 9, "bold"),
    fg=ACENTO,
    bg=FONDO,
).pack(anchor="w")
tk.Label(
    contenedor,
    text="Fórmula general",
    font=("Arial", 23, "bold"),
    fg=TEXTO,
    bg=FONDO,
).pack(anchor="w", pady=(5, 2))
tk.Label(
    contenedor,
    text="Resuelve una ecuación de la forma ax² + bx + c = 0",
    font=("Arial", 10),
    fg=SECUNDARIO,
    bg=FONDO,
).pack(anchor="w", pady=(0, 20))

formulario = tk.Frame(contenedor, bg=TARJETA, padx=20, pady=17)
formulario.pack(fill="x")
entradas = {}
for fila, nombre, descripcion in (
    (0, "a", "Término cuadrático"),
    (1, "b", "Término lineal"),
    (2, "c", "Término independiente"),
):
    tk.Label(
        formulario,
        text=f"{nombre}  ·  {descripcion}",
        font=("Arial", 10, "bold"),
        fg=TEXTO,
        bg=TARJETA,
    ).grid(row=fila * 2, column=0, sticky="w", pady=(5, 2))
    entrada = tk.Entry(
        formulario,
        width=30,
        font=("Arial", 12),
        relief="flat",
        bg="#253449",
        fg=TEXTO,
        insertbackground=TEXTO,
    )
    entrada.grid(row=fila * 2 + 1, column=0, sticky="ew", pady=(0, 6))
    entradas[nombre] = entrada

formulario.columnconfigure(0, weight=1)
entrada_a, entrada_b, entrada_c = entradas["a"], entradas["b"], entradas["c"]

acciones = tk.Frame(contenedor, bg=FONDO)
acciones.pack(fill="x", pady=16)

boton = tk.Button(
    acciones,
    text="Calcular raíces  →",
    command=calcular_raices,
    font=("Arial", 11, "bold"),
    bg=ACENTO,
    fg="#082032",
    activebackground="#7dd3fc",
    activeforeground="#082032",
    relief="flat",
    cursor="hand2",
    padx=14,
    pady=10,
)
boton.pack(side="left", expand=True, fill="x")
boton.bind("<Enter>", lambda evento: boton.configure(bg="#7dd3fc"))
boton.bind("<Leave>", lambda evento: boton.configure(bg=ACENTO))

boton_limpiar = tk.Button(
    acciones,
    text="Limpiar",
    command=limpiar_campos,
    font=("Arial", 10, "bold"),
    bg="#334155",
    fg=TEXTO,
    activebackground="#475569",
    activeforeground=TEXTO,
    relief="flat",
    cursor="hand2",
    padx=10,
    pady=10,
)
boton_limpiar.pack(side="left", padx=(10, 0), fill="x")

boton_salir = tk.Button(
    acciones,
    text="Salir",
    command=salir_aplicacion,
    font=("Arial", 10, "bold"),
    bg="#7f1d1d",
    fg=TEXTO,
    activebackground="#991b1b",
    activeforeground=TEXTO,
    relief="flat",
    cursor="hand2",
    padx=10,
    pady=10,
)
boton_salir.pack(side="left", padx=(10, 0), fill="x")

tk.Label(
    contenedor,
    text="RESULTADO",
    font=("Arial", 9, "bold"),
    fg=ACENTO,
    bg=FONDO,
).pack(anchor="w", pady=(2, 7))
resultado = tk.Label(
    contenedor,
    text="Introduce los coeficientes para ver las soluciones.",
    justify="left",
    anchor="w",
    font=("Consolas", 11),
    fg=TEXTO,
    bg=TARJETA,
    padx=16,
    pady=14,
    wraplength=370,
)
resultado.pack(fill="x")
ventana.bind("<Return>", lambda evento: calcular_raices())
entrada_a.focus_set()

ventana.mainloop()

