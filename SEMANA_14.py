import tkinter as tk
from tkinter import messagebox
import sqlite3


# Función para agregar un evento a la base de datos
def agregar_evento():
    titulo = entry_titulo.get()
    fecha = entry_fecha.get()
    descripcion = entry_descripcion.get()

    if titulo and fecha and descripcion:
        conn = sqlite3.connect('agenda.db')
        c = conn.cursor()
        c.execute("INSERT INTO eventos (titulo, fecha, descripcion) VALUES (?, ?, ?)", (titulo, fecha, descripcion))
        conn.commit()
        conn.close()
        messagebox.showinfo("Evento agregado correctamente")
        entry_titulo.delete(0, tk.END)
        entry_fecha.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Todos los campos son obligatorios")


# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("400x200")

# Crear y colocar los widgets
tk.Label(root, text="Título").grid(row=0, column=0)
entry_titulo = tk.Entry(root)
entry_titulo.grid(row=0, column=1)

tk.Label(root, text="Fecha (YYYY-MM-DD)").grid(row=1, column=0)
entry_fecha = tk.Entry(root)
entry_fecha.grid(row=1, column=1)

tk.Label(root, text="Descripción").grid(row=2, column=0)
entry_descripcion = tk.Entry(root)
entry_descripcion.grid(row=2, column=1)

tk.Button(root, text="Agregar Evento", command=agregar_evento).grid(row=3, column=0, columnspan=2)

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
