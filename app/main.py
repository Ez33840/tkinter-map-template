from tkinter import*
from controller.controlador_principal import ControladorPrincipal

from tkintermapview import TkinterMapView

root = Tk()
root.title("Recitales musicales")
controlador = ControladorPrincipal(root)

root.geometry("1100x700")



root.mainloop()
