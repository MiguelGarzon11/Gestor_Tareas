# interfaz.py
import tkinter as tk
from tareas import SimpleTask

class TaskApp:
    def __init__(self, root, storage, manager):
        self.storage = storage
        self.manager = manager
        self.root = root
        self.root.title("Gestor de Tareas")

        # Widgets
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.add_button = tk.Button(self.root, text="Agregar tarea", command=self.agregar_tarea)
        self.add_button.pack()

        self.complete_button = tk.Button(self.root, text="Marcar como completa", command=self.marcar_completada)
        self.complete_button.pack()

        self.delete_button = tk.Button(self.root, text="Eliminar tarea", command=self.eliminar_tarea)
        self.delete_button.pack()

        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.pack()

        self.refresh_view()

    def agregar_tarea(self):
        descripcion = self.entry.get()
        if descripcion:
            nueva_tarea = SimpleTask(id=len(self.manager.tasks) + 1, descripcion=descripcion)
            self.manager.agregar_tarea(nueva_tarea)
            self.storage.guardar_tareas(self.manager.tasks)
            self.refresh_view()

    def eliminar_tarea(self):
        selected_task = self.task_listbox.get(tk.ACTIVE)
        if selected_task:
            task_id = int(selected_task.split()[0])
            self.manager.eliminar_tarea(task_id)
            self.storage.guardar_tareas(self.manager.tasks)
            self.refresh_view()

    def marcar_completada(self):
        selected_task = self.task_listbox.get(tk.ACTIVE)
        if selected_task:
            task_id = int(selected_task.split()[0])
            self.manager.marcar_completada(task_id)
            self.storage.guardar_tareas(self.manager.tasks)
            self.refresh_view()

    def refresh_view(self):
        self.task_listbox.delete(0, tk.END)
        for tarea in self.manager.tasks:
            estado = "Completada" if tarea.completada else "Pendiente"
            self.task_listbox.insert(tk.END, f"{tarea.id} {tarea.descripcion} - {estado}")
