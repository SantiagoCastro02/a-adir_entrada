import tkinter as tk
from tkinter import ttk

# lista de frutas con sus colores
frutas = {
    "rojo": "manzana",
    "naranja": "naranja",
    "amarillo": "limón",
    "verde": "kiwi",
    "azul": "arándano",
    "morado": "uva"
}

# función que se ejecuta cuando se selecciona una opción del combobox
def mostrar_fruta(*args):
    color = combo_color.get().lower()
    fruta = frutas.get(color)
    if fruta:
        etiqueta_fruta.config(text=fruta)
    else:
        etiqueta_fruta.config(text="No se encontró ninguna fruta para ese color.")

# crear la ventana
ventana = tk.Tk()
ventana.title("Frutas por color")

# crear el combobox y el botón
etiqueta_color = ttk.Label(ventana, text="Seleccione un color:")
etiqueta_color.pack()
colores = list(frutas.keys())
combo_color = ttk.Combobox(ventana, values=colores)
combo_color.pack()
combo_color.bind("<<ComboboxSelected>>", mostrar_fruta)

# crear la etiqueta para mostrar la fruta
etiqueta_fruta = ttk.Label(ventana, text="")
etiqueta_fruta.pack()

# iniciar el loop de la ventana
ventana.mainloop()
