import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.tareas = []

        # Campo de entrada para nuevas tareas
        self.entry_tarea = tk.Entry(root, width=40)
        self.entry_tarea.grid(row=0, column=0, padx=10, pady=10)

        # Botones
        self.btn_agregar = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        self.btn_agregar.grid(row=0, column=1, padx=5, pady=10)

        self.btn_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.btn_completar.grid(row=1, column=0, padx=5, pady=5)

        self.btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=1, column=1, padx=5, pady=5)

        # Lista de tareas
        self.lista_tareas = tk.Listbox(root, width=50, height=10)
        self.lista_tareas.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Enlazar la tecla Enter al botón "Añadir Tarea"
        self.entry_tarea.bind("<Return>", lambda event: self.agregar_tarea())

        # Enlazar doble clic a la lista para marcar como completada
        self.lista_tareas.bind("<Double-Button-1>", lambda event: self.marcar_completada())

    def agregar_tarea(self):
        tarea = self.entry_tarea.get()
        if tarea:
            self.tareas.append({"tarea": tarea, "completada": False})
            self.actualizar_lista()
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.tareas[indice]["completada"] = True
            self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.tareas[indice]
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            estado = "[Completada]" if tarea["completada"] else "[Pendiente]"
            self.lista_tareas.insert(tk.END, f"{estado} {tarea['tarea']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()