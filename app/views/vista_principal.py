import tkinter as tk
from tkinter import ttk
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk

class VistaPrincipal:
    def __init__(self, root, seleccionar_evento_callback=None, seleccionar_ubicacion_callback=None):
        self.root = root
        self.seleccionar_evento_callback = seleccionar_evento_callback
        self.seleccionar_ubicacion_callback = seleccionar_ubicacion_callback
        self.frame_mapa = tk.Frame(self.root, width=600, height=600)
        self.frame_mapa.pack(side='right')

        self.frame_evento = tk.Frame(self.root, width=300, height=600)
        self.frame_evento.pack(side='left', fill='both', expand=True)

        # Placeholder para el mapa
        self.mapa = TkinterMapView(self.frame_mapa, width=800, height=800, corner_radius=0)
        self.mapa.set_position(-34.593943583296124, -58.44805849014205)
        self.mapa.set_zoom(16)
        self.mapa.pack(side='right')

        # Listbox para los locales
        self.lista_evento = tk.Listbox(self.frame_evento)
        self.lista_evento.bind('<<ListboxSelect>>', seleccionar_evento_callback)
        self.lista_evento.pack(fill='both', expand=True)

    def agregar_evento(self, evento):
        nombre = evento.nombre
        self.lista_evento.insert(tk.END, nombre)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_ubicacion_callback)


