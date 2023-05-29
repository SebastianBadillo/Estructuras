# El director de un hotel desea implementar una sistema de administración para saber la disponibilidad y asignación de habitaciones. Para asignar, registra el número de cédula y el nombre de cada cliente a medida que llega al hotel, junto con el número de habitación que ocupa (el antiguo libro de entradas).

# Igualmente cuando un huésped se retira del hotel se actualiza la disponibilidad de las habitaciones, el libro de entradas y el libro de salida.

# El director desea en un momento dado contar con la siguiente información:
# Consultas vigentes por huésped: (1) Individual y (2) total. Las consultas (2) totales pueden ser: (1) Por cédula y (2) por orden de llegada. 
# Para cualquiera de las consultas entregar toda la información asociada al huésped.
# Consulta de habitaciones: (1) Lista de habitaciones disponibles y (2) Lista de habitaciones ocupadas.
from datetime import datetime

import listas as li
class Habitacion:
    def __init__(self, habitacion, huesped = '', cedula = 0, disponible = True, fecha_entrada='', fecha_salida = ''):
        self.habitacion = habitacion
        self.huesped = huesped
        self.cedula = cedula
        self.disponible = disponible
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida


    
class Hotel():
    def __init__(self):
        self.limpieza()
        self.libro_salida = li.Lista()

    def ingreso_huesped(self, nombre, cedula, fecha):
        for x in self.libro_entrada:
            if x.disponible == True:
                x.huesped = nombre
                x.cedula = cedula
                x.fecha_entrada = fecha
                x.disponible = False
                return 0
                
    def salida_huesped(self, nombre, cedula):
        for x in self.libro_entrada:
            if x.huesped == nombre and x.cedula == cedula:
                x.fecha_salida = datetime.now()
                fecha = datetime.now()
                a = self.libro_entrada[x]
                self.libro_salida.agregar_al_inicio(Habitacion(a.habitacion, a.huesped, False, a.fecha_entrada, fecha)) # type: ignore
                x.huesped = ''
                x.cedula = 0
                x.fecha_entrada = ''
                x.disponible = True

    def situacion_actual(self):
        print('SITUACION HOTEL:')
        for x in self.libro_entrada:
            if x.disponible == True:
                print(f'Habitacion {x.habitacion} esta desocupada')
            else:
                print(f'Habitacion {x.habitacion} ocupada por: {x.huesped}')
    def limpieza(self):
        self.libro_entrada = li.Lista()
        for x in range(0,10):
            self.libro_entrada.agregar_al_final(Habitacion(x+1))