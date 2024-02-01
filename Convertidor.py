import tkinter as tk
from tkinter import ttk

class Convertidor:
    def __init__(self):
        self.peso = 1
        self.dolar = 1

    def peso_to_dolar(self, peso):
        return peso * 0.00025

    def dolar_to_peso(self, dolar):
        return dolar * 3991

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
marco.grid(padx=20, pady=20)

lbl_titulo = ttk.Label(marco, text="Convertidor de divisa", font=("Arial", 16))
lbl_titulo.grid(column=0, row=0, columnspan=3)

lbl_operacion = ttk.Label(marco, text="Selecciona una moneda:")
lbl_operacion.grid(column=0, row=1, sticky=tk.W)

opcion_operacion = tk.IntVar()
radio_cop_to_usd = ttk.Radiobutton(marco, text="COP to USD", variable=opcion_operacion, value=1)
radio_cop_to_usd.grid(column=1, row=1)
radio_usd_to_cop = ttk.Radiobutton(marco, text="USD to COP", variable=opcion_operacion, value=2)
radio_usd_to_cop.grid(column=2, row=1)

lbl_cantidad = ttk.Label(marco, text="Cantidad:")
lbl_cantidad.grid(column=0, row=2, sticky=tk.W)

entry_cantidad = ttk.Entry(marco)
entry_cantidad.grid(column=1, row=2)

btn_convertir = ttk.Button(marco, text="Convertir", command=convertir)
btn_convertir.grid(column=0, row=3, columnspan=3, pady=10)

lbl_resultado = ttk.Label(marco, text="Resultado:")
lbl_resultado.grid(column=0, row=4, columnspan=3)

ventana.mainloop()
