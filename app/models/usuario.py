import json

class Usuario:
    def __init__(self, id_usuario, nombre, apellido, historial_eventos):
        self. id_usuario= id_usuario
        self. nombre= nombre
        self. apellido= apellido
        self. historial_eventos= historial_eventos

        def a_json(self):
            return json.dumps(self.__dict__)
        
        @classmethod
        def a_json(cls, datos_json):
            datos= json.loads(datos_json)
            return cls(**datos)
        
        @staticmethod
        def cargar_usuarios(archivo_json):
            with open(archivo_json, "r") as archivo:
                datos= json.load(archivo)
            return [Usuario.de_json(json.dumps(dato)) for dato in datos]