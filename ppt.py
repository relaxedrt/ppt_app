import random as r

#FUNCIONES
def ppt(us):
    res = ""
    m = r.randint(1,3)
    if us == 1:
        if m == 1:
            res = "Piedra vs Piedra, nos quedamos igual."
        if m == 2:
            res = "Piedra pierde contra papel y pierdes"
        if m == 3:
            res = "Piedra aplasta las tijeras y ganas"
    if us == 2:
        if m == 1:
            res = "Papel gana a piedra y ganas"
        if m == 2:
            res = "Papel vs Papel, nos quedamos igual."
        if m == 3:
            res = "Las tijeras cortan tu papel y pierdes"
    if us == 3:
        if m == 1:
            res = "Tijeras pierden contra piedra y pierdes"
        if m == 2:
            res = "Tijeras cortan el papel y ganas"
        if m == 3:
            res = "Tijeras vs Tijeras, nos quedamos igual."
    print(res)
    
ppt(int(input("Piedra 1, Papel 2, Tijera 3: ")))
