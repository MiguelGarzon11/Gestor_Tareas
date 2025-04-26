import json

class JSONAlmacenamiento:
    def __init__(self, ruta):
        self.ruta = ruta

    def cargar_tareas(self):
        try:
            with open(self.ruta, 'r') as archivo:
                contenido = archivo.read().strip()
                if not contenido:
                    return []
                return json.loads(contenido)   # Permite cargar el contenido del archivo JSON en un objeto Python(lsita o diccionario)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def guardar_tareas(self, tareas):
        with open(self.ruta, 'w') as archivo:   # Se abre un archivo en modo escritura, Si el archivo no exite se crea y si existe se remplaza.
            json.dump([tarea.to_dict() for tarea in tareas], archivo)   # json.dump(permite escribir datos en un archivo fromato JSON)