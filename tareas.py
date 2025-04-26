class Tarea:
    def __init__(self, id, descripcion):
        self.id = id
        self.descripcion = descripcion
        self.completada = False

    def to_dict(self):
        return {"id": self.id, "descripcion": self.descripcion, "completada": self.completada}
    
    def marcar_completada(self):
        self.completada = True

class SimpleTarea(Tarea):
    pass

class Recurring(Tarea):
    def __init__(self, id, descripcion, intervalo):
        super().__init__(id, descripcion)
        self.intervalo = intervalo

    def to_dict(self):
        data = super().to_dict()
        data["intervalo"] = self.intervalo
        return data
    