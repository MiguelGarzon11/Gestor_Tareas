import os
os.environ["LIBXCB_ALLOW_SLOPPY_LOCK"] = "1"

import tkinter as tk
from tkinter import ttk

from tareas import Recurring, SimpleTask, TaskManager
from almacenamiento import JSONAlmacenamiento
from interfaz import TaskApp


def main():
    print("Iniciando aplicación...")
    almacenamiento = JSONAlmacenamiento("tareas.json")
    print("Archivo de almacenamiento cargado.")
    
    datos = almacenamiento.cargar_tareas()
    print(f"Tareas cargadas: {datos}")

    manager = TaskManager()
    print("Gestor de tareas creado.")

    for d in datos:
        if "intervalo" in d:
            tarea = Recurring(d["id"], d["descripcion"], d["intervalo"])
        else:
            tarea = SimpleTask(d["id"], d["descripcion"])
        if d.get("completada"):
            tarea.marcar_completada()
        manager.agregar_tarea(tarea)
    print("Tareas procesadas.")

    root = tk.Tk()
    print("Ventana creada.")
    app = TaskApp(root, almacenamiento, manager)
    print("App cargada.")
    app.root.mainloop()

if __name__ == "__main__":
    main()