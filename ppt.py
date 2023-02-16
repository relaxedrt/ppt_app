#Importamos todas las librerias necesarias para la visualiacion de la app
import tkinter
import customtkinter as tk
import random as r

#Le damos una tonalidad a la app
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

#Le damos titulo y tamano a la app
app = tk.CTk()
app.geometry("300x400")
app.title("Piedra Papel Tijeras")

#FUNCIONES
def ppt(us):
    res = ""
    m = r.randint(1,3)
    if us == 0:
        if m == 0:
            res = "Draw."
        if m == 1:
            res = "Gana la maquina."
        if m == 2:
            res = "Ganas tu."
    if us == 1:
        if m == 0:
            res = "Ganas tu."
        if m == 1:
            res = "Draw."
        if m == 2:
            res = "Ganas la maquina."
    if us == 2:
        if m == 0:
            res = "Ganas la maquina."
        if m == 1:
            res = "Ganas tu."
        if m == 2:
            res = "Draw."
    

#Creamos la variable del resultado y definimos el texto que lo mostrara
""" res = "Selecciona una opcion."
result = tk.CTkLabel(master=app, text=res)
result.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER) """

#Creamos los botones de cada opcion
piedra = tk.CTkButton(master = app, text="Piedra", command = ppt(1))
piedra.place(relx=0.5, rely=0.075, anchor=tkinter.CENTER)

papel = tk.CTkButton(master = app, text="Papel", command = ppt(2))
papel.place(relx=0.5, rely=0.175, anchor=tkinter.CENTER)

tijera = tk.CTkButton(master = app, text="Tijera", command = ppt(3))
tijera.place(relx=0.5, rely=0.275, anchor=tkinter.CENTER)

#Ejecutamos la aplicacion
app.mainloop()