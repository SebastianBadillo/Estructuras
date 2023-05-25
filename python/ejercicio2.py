"""
2. Suponga que en la UIS hay 6500 estudiantes. Por cada uno de ellos tenemos un registro con el código, nombre y promedio acumulado. Hacer el programa que:

Imprima el código y el nombre de los estudiantes de la carrera X(debe leerse el código de la carrera a listar) que tengan promedio acumulado igual o mayor a 4 y decir cuántos fueron.
Imprima el código y el nombre de los estudiantes que ingresaron antes de 1990 y están condicionales.
"""

# Daniel Sebastian Badillo Neira 2220071
import numpy as np
import random as r


def ViejosYCondicionales():

    for estudiante in estudiantes:
        if (estudiante['añoIngreso'] < 1990 and estudiante['promedio'] <= 3.2):
            print(estudiante)


def ImprimirPorCarrera():
    print("""
        ¿Que carrera desea listar?
        Oprima:
        0) Ing Sistemas
        1) Matematicas
        2) Fisica
        3) Quimica
    """)
    rta = int(input())
    if ((rta == 0) or (rta == 1) or (rta == 2) or (rta == 3)):
        carrera = carreras[rta]
        contador = 0
        for estudiante in estudiantes:
            if (estudiante['carrera'] == carrera and estudiante['promedio'] >= 4):
                print(estudiante)
                contador += 1
        print(contador)
    else:
        ImprimirPorCarrera()


# Nombres predeterminados
nombres = ['Juan', 'Pedro', 'Maria', 'Silvia']
# Carreras predeterminadas
carreras = ['0- Ing.Sistemas', '1-Matematicas', '2-Fisica', '3-Quimica']

# defino la estructura de mi array
tipo = np.dtype(
    [
        ('codigo', int),
        ('carrera', 'U20'),
        ('nombre', 'U20'),
        ('promedio', float),
        ('añoIngreso', int)
    ]
)

estudiantes = np.zeros(6500, dtype=tipo)  # Creo el array estudiantes
codigo = 1

for x in range(0, 6500):  # Ciclo for para dar informacion a los 6500 estudiantes
    aleatorio = r.randint(0, 3)
    aleatorio2 = r.randint(0, 3)
    promedio = r.uniform(2.8, 5)
    añoIngreso = r.randint(1980, 2023)
    estudiantes[x] = codigo, carreras[aleatorio2], nombres[aleatorio], round(
        promedio, 2), añoIngreso
    codigo += 1


print("""
    ¿ Que desea hacer ?
    0) Imprimir los estudiantes por carreras y promedio mayor a 4
    1) Imprimir estudiantes que ingresaron antes de 1990 y los condicioneales

""")
op = int(input())

if (op == 0):
    ImprimirPorCarrera()
elif (op == 1):
    ViejosYCondicionales()
else:
    print("Error al introducir los datos")
