import tkinter as tk
from tkinter import ttk

class Convertidor:
    def __init__(self):
        self.peso = 1
        self.dolar = 1
        self.libras = 1
        self.soles = 1
        self.reales = 1

#pesos
    def peso_to_dolar(self, peso):
        return peso * 0.00025
    def peso_to_libras(self, peso):
        return peso * 0.00020
    def peso_to_soles(self, peso):
        return peso * 0.0041
    def peso_to_reales(self, peso):
        return peso * 0.0041

#dolares
    def dolar_to_peso(self, dolar):
        return dolar * 3,933.50
    def dolar_to_libras(self, dolar):
        return dolar * 0.79
    def dolar_to_soles(self, dolar):
        return dolar * 3.81
    def dolar_to_reales(self, dolar):
        return dolar * 4.95

#libras
    def libras_to_dolar(self, libras):
        return libras * 1.26
    def libras_to_pesos(self, libras):
        return libras * 4,969.19
    def libras_to_soles(self, libras):
        return libras * 4.81
    def libras_to_reales(self, libras):
        return libras * 6.25

#soles
    def soles_to_dolar(self, soles):
        return soles * 0.26
    def soles_to_libras(self, soles):
        return soles * 0.21
    def soles_to_peso(self, soles):
        return soles * 1,033.50
    def soles_to_reales(self, soles):
        return soles * 1.30

#reales
    def reales_to_dolar(self, reales):
        return reales * 0.20
    def reales_to_libras(self, reales):
        return reales * 0.16
    def reales_to_soles(self, reales):
        return reales * 0.77
    def reales_to_peso(self, reales):
        return reales * 795.33

def convertir():
    cantidad = float(entry_cantidad.get())
    operacion = opcion_operacion.get()
    if operacion == 1:
        resultado = Converter_currency.peso_to_dolar(cantidad)
        lbl_resultado["text"] = f"Resultado: {resultado} $"
    elif operacion == 2:
        resultado = Converter_currency.dolar_to_peso(cantidad)
        lbl_resultado["text"] = f"Resultado: {resultado} $"

Converter_currency = Convertidor()
ventana = tk.Tk()
ventana.title("Convertidor")

marco = ttk.Frame(ventana, padding=10)
marco.grid(padx=0, pady=0)

lbl_titulo = ttk.Label(marco, text="Convertidor de divisa", font=("Arial", 16)).grid(padx=100, pady=0, row=0, sticky=tk.W)
lbl_operacion = ttk.Label(marco, text="Selecciona una moneda:").grid(padx=135, pady=0, row=1, sticky=tk.W)

opcion_operacion = tk.IntVar()
radio_peso = ttk.Radiobutton(marco, text="Pesos colombianos", variable=opcion_operacion, value=1).grid(column=0, row=2, sticky=tk.W)
radio_dolar = ttk.Radiobutton(marco, text="Dolar", variable=opcion_operacion, value=2).grid(column=0, row=3, sticky=tk.W)
boton = ttk.Button(marco, text="Convertir", command=convertir).grid(padx=150, pady=0, sticky=tk.W)
radio_libras = ttk.Radiobutton(marco, text="Libras Esterlinas", variable=opcion_operacion, value=3).grid(column=0, row=4, sticky=tk.W)
radio_soles = ttk.Radiobutton(marco, text="Sol peruano", variable=opcion_operacion, value=4).grid(column=0, row=5, sticky=tk.W)
radio_reales = ttk.Radiobutton(marco, text="Real brasileño", variable=opcion_operacion, value=5).grid(column=0, row=6, sticky=tk.W)

opcion_convertir = tk.IntVar()
radio_peso = ttk.Radiobutton(marco, text="Pesos colombianos", variable=opcion_convertir, value=1).grid(padx=270, pady=0, row=2, sticky=tk.W)
radio_dolar = ttk.Radiobutton(marco, text="Dolar", variable=opcion_convertir, value=2).grid(padx=270, pady=0, row=3, sticky=tk.W)
radio_libras = ttk.Radiobutton(marco, text="Libras Esterlinas", variable=opcion_convertir, value=3).grid(padx=270, pady=0, row=4, sticky=tk.W)
radio_soles = ttk.Radiobutton(marco, text="Sol peruano", variable=opcion_convertir, value=4).grid(padx=270, pady=0, row=5, sticky=tk.W)
radio_reales = ttk.Radiobutton(marco, text="Real brasileño", variable=opcion_convertir, value=5).grid(padx=270, pady=0, row=6, sticky=tk.W)
lbl_resultado = ttk.Label(marco, text="Resultado:").grid(padx=270, pady=0, row=7, sticky=tk.W)

lbl_cantidad = ttk.Label(marco, text="Cantidad:").grid(column=0, row=7, sticky=tk.W)
entry_cantidad = ttk.Entry(marco).grid(padx=55, pady=0, row=7, sticky=tk.W)

ventana.mainloop()