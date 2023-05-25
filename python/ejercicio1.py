# En la universidad se efectuó la elección del representante de los estudiantes ante el Consejo Superior. Se presentaron 30 candidatos y cada uno se identificó con un número del 1 al 30. Asumiendo que los 5000 estudiantes de la universidad votaron, elabore un programa donde:

# Imprima un listado de mayor a menor, según el número de votos obtenidos por cada candidato


# Daniel Sebastian Badillo Neira 2220071
import numpy as np
import random as r


# Defino la estructura de mi array
tipo = np.dtype([('Nombre', 'U20'), ('votos', int)])
candidatos = np.ones(30, dtype=tipo)  # Creo un array con 30 posiciones


for x in range(0, 30):  # Ciclo for para llenar el arreglo candidatos
    temp = f"Candidato {x + 1}", 0
    candidatos[x] = temp


for x in range(0, 5000):  # Simulación de votos
    indiceAleatorio = r.randint(0, 29)
    candidatos[indiceAleatorio]['votos'] += 1

# Ordeno los votos
listaOrdenada = np.sort(candidatos, order='votos')[::-1]

for x in listaOrdenada:
    print(x)
