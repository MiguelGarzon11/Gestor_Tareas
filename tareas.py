class Task:
    def __init__(self, id, descripcion):
        self.id = id
        self.descripcion = descripcion
        self.completada = False

    def to_dict(self):
        return {"id": self.id, "descripcion": self.descripcion, "completada": self.completada}
    
    def marcar_completada(self):
        self.completada = True

class SimpleTask(Task):
    pass

class Recurring(Task): 
    def __init__(self, id, descripcion, intervalo):
        super().__init__(id, descripcion)
        self.intervalo = intervalo

    def to_dict(self):
        data = super().to_dict()
        data["intervalo"] = self.intervalo
        return data
    
class TaskManager:
    def __init__(self):
        self.tasks = []

    def agregar_tarea(self, tarea):
        self.tasks.append(tarea)
    
    def eliminar_tarea(self, tarea_id):
        self.tasks = [tarea for tarea in self.tasks if tarea.id != tarea_id]

    def marcar_completada(self, tarea_id):
        for tarea in self.tasks:
            if tarea.id == tarea_id:
                tarea.marcar_completada()

    def get_all_tasks(self):
        return self.tasks
    

    