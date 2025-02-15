import json

class Evento:
    def __init__(self,id, nombre, artista ,genero ,id_ubicacion ,hora_inicio , hora_fin, descripcion ,imagen,):
        self.id=id
        self.nombre = nombre
        self.artista=artista
        self.genero=genero
        self.id_ubicacion=id_ubicacion
        self.hora_inicio=hora_inicio
        self.hora_fin=hora_fin
        self.descripcion=descripcion
        self.imagen = imagen


    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def cargar_eventos(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Evento.de_json(json.dumps(dato)) for dato in datos]