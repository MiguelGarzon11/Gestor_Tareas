# Interfaz gráfica y gestión de tareas

import tkinter as tk
from tkinter import messagebox

class TaskApp:
    def __init__(self, storage, manager):
        self.storage = storage
        self.manager = manager
        self.root = tk.Tk() # Crea la ventana principal
        self.root.title("Gestor de Tareas") # Establece el título de la ventana

        # Widgets
        self.entry = tk.Entry(self.root) # Campo de texto donde se escribe la nueva tarea.
        self.entry.pack() # Organiza visualmente el widget.

        self.add_button = tk.Button(self.root, text="Agregar tarea", command=self.agregar_tarea) # Se crea un boton y con el command se llama a la función agregar_tarea al hacer click
        self.add_button.pack() # Muestra el boton en pantalla

        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.pack() # Muestra la lista en pantalla

        self.refresh_view() # Llama a la función refresh_view para mostrar la lista de tareas al iniciar.

    def agregar_tarea(self):
        descripcion = self.entry.get() # get() obtiene el texto escrito por el usuario.
        if descripcion: # Si el campo no esta vacío.
            nueva_tarea = SimpleTask(id=len(self.manager.tasks)+1, descripcion=descripcion)
            self.manager.agregar_tarea(nueva_tarea)
            self.storage.guardar_tareas(self.manager.task)
            self.refresh_view()

    def eliminar_tarea(self):
        selected_task = self.task_listbox.get(tk.ACTIVATE)
        if selected_task:
            task_id = int(selected_task.split()[0]) # Asumiendo formato "ID Descripción"
            self.manager.marcar_completada(task_id)
            self.storage.guardar_tareas(self.manager.tasks)
            self.refresh_view()

    def marcar_completada(self):
        selected_task = self.task_listbox.get(tk.ACTIVATE)
        if selected_task:
            task_id = int(selected_task.split()[0])
            self.manager.marcar_completada(task_id)
            self.storage.guardar_tareas(self.manager.tasks)
            self.refresh_view()

    def refresh_view(self):
        self.task_listbox.delete(0, tk.END)
        for tarea in self.manager.tasks:
            self.task_listbox.insert(tk.END, f"{tarea.id} {tarea.descripcion} - {'Completada' if tarea.completada else 'Pendiente'}")

    def run(self):
        self.root.mainloop()






