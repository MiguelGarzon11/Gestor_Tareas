import ctypes
ctypes.CDLL("libX11.so.6").XInitThreads()


import tkinter as tk
from tareas import SimpleTask, Recurring, TaskManager
from almacenamiento import JSONAlmacenamiento
from interfaz import TaskApp

def main():
    almacenamiento = JSONAlmacenamiento("tareas.json")
    datos = almacenamiento.cargar_tareas()
    manager = TaskManager()

    for d in datos:
        if "intervalo" in d:
            tarea = Recurring(d["id"], d["descripcion"], d["intervalo"])
        else:
            tarea = SimpleTask(d["id"], d["descripcion"])
        if d.get("completada"):
            tarea.marcar_completada()
        manager.agregar_tarea(tarea)

    root = tk.Tk()
    app = TaskApp(root, almacenamiento, manager)
    app.root.mainloop()

if __name__ == "__main__":
    main()