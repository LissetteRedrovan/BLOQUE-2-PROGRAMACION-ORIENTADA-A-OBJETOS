import tkinter as tk

def agregar_dato():
    dato = entrada.get()
    if dato:
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)

def limpiar_lista():
    lista.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos")

# Componentes de la interfaz
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack()

lista = tk.Listbox(ventana)
lista.pack()

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack()

# Bucle principal de la aplicación
ventana.mainloop()
