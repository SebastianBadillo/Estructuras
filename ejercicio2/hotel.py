# El director de un hotel desea implementar una sistema de administración para saber la disponibilidad y asignación de habitaciones. Para asignar, registra el número de cédula y el nombre de cada cliente a medida que llega al hotel, junto con el número de habitación que ocupa (el antiguo libro de entradas).

# Igualmente cuando un huésped se retira del hotel se actualiza la disponibilidad de las habitaciones, el libro de entradas y el libro de salida.

# El director desea en un momento dado contar con la siguiente información:
# Consultas vigentes por huésped: (1) Individual y (2) total. Las consultas (2) totales pueden ser: (1) Por cédula y (2) por orden de llegada. 
# Para cualquiera de las consultas entregar toda la información asociada al huésped.
# Consulta de habitaciones: (1) Lista de habitaciones disponibles y (2) Lista de habitaciones ocupadas.
import numpy as np
import random as r
tipo = np.dtype(
    [
        ('habitacion', int),
        ('nombre','U20'),
        ('cedula', int),
        ('disponibilidad', bool)
    ]
)




class Hotel:
    def __init__(self):
        self.vaciar()
        self.habitaciones_disponibles = [1,2,3,4,5,6,7,8,9,10]
        self.habitaciones_ocupadas =[]
    
    def vaciar(self):
        self.registro = np.ones(10, dtype=tipo)
        for x in range(1,11):
            self.registro[x-1]= x , '', 0, True

    def asignar_habitacion(self, nombre, cedula):
        key = False
        if len(self.habitaciones_disponibles) != 0:
            for habitacion in self.registro:
                if habitacion['disponibilidad'] == True:
                    
                    habitacion['nombre'] = nombre
                    habitacion['cedula'] = cedula
                    habitacion['disponibilidad'] = False
                    key = True
                    self.habitaciones_disponibles.remove(habitacion['habitacion'])
                    self.habitaciones_ocupadas.append(habitacion['habitacion'])
                    return f"El registro ha sido exitoso, su habitación es {habitacion['habitacion']}"
        if key== False:
            return 'No hay habitaciones disponibles'
    
    def salida_huesped(self, nombre, cedula):
        key = False
        for habitacion in self.registro:
            if habitacion['nombre'] == nombre and habitacion['cedula'] == cedula:
                text = f"Hasta la proxima huesped {str(habitacion['nombre'])}"
                key = True
                habitacion['nombre'] = ''
                habitacion['cedula'] = 0
                habitacion['disponibilidad'] = True
                self.habitaciones_disponibles.append(habitacion['habitacion'])
                self.habitaciones_disponibles.sort()
                self.habitaciones_ocupadas.remove(habitacion['habitacion'])
                return text
        if key == False:
            return f"El usuario no es huesped de este hotel"

    def situacion_actual(self):
        for habitacion in self.registro:
            if habitacion['disponibilidad'] == False:
                print(f"La habitacion {habitacion['habitacion']} esta ocupada por {habitacion['nombre']} con cedula {habitacion['cedula']}")
            else:
                print(f"La habitacion {habitacion['habitacion']} no esta ocupada")
                
    def consulta_habitaciones(self):
        print('HABITACIONES DISPONIBLES: ')
        for x in self.habitaciones_disponibles:
            print(f"Habitacion {x}")
        print('HABITACIONES NO DISPONIBLES: ')
        for x in self.habitaciones_ocupadas:
            print(f"Habitacion {x}")
    
    def getDisponibles(self):
        return self.habitaciones_disponibles
    def getOcupadas(self):
        return self.habitaciones_ocupadas
    def getregistro(self):
        return self.registro


from datetime import datetime

# Solicitar fecha al usuario
fecha_str = input("Ingrese una fecha (formato: dd/mm/aaaa): ")

# Convertir la cadena a un objeto datetime
fecha = datetime.strptime(fecha_str, "%d/%m/%Y")

# Imprimir la fecha ingresada
print("Fecha ingresada:", fecha)