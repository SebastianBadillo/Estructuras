import hotel as h

# El director de un hotel desea implementar una sistema de administración para saber la disponibilidad y asignación de habitaciones. Para asignar, registra el número de cédula y el nombre de cada cliente a medida que llega al hotel, junto con el número de habitación que ocupa (el antiguo libro de entradas).

# Igualmente cuando un huésped se retira del hotel se actualiza la disponibilidad de las habitaciones, el libro de entradas y el libro de salida.

# El director desea en un momento dado contar con la siguiente información:
# Consultas vigentes por huésped: (1) Individual y (2) total. Las consultas (2) totales pueden ser: (1) Por cédula y (2) por orden de llegada. 
# Para cualquiera de las consultas entregar toda la información asociada al huésped.
# Consulta de habitaciones: (1) Lista de habitaciones disponibles y (2) Lista de habitaciones ocupadas.

def guia():
    print("""
    Bienvenido:
    ¿Qué desea realizar?
    1. Añadir huesped
    2. Despedir huesped
    3. Consulta de habitaciones
    4. Salir
    """)
    respuesta = int(
        input("¿ Que desea realizar el dia de hoy ? [Digite un numero entre 1 y 3] "))
    return respuesta

def opcion1():
    print("Okey vamos a añadir huesped")
    nombre = input('Ingrese el nombre del huesped: ')
    cedula = int(input('Ingrese la cedula del huesped: '))
    print(hotel.asignar_habitacion(nombre, cedula))

def opcion2():
    print('Okey Vamos a despedir huesped')
    nombre = input('Ingrese el nombre del huesped: ')
    cedula = int(input('Ingrese la cedula del huesped: '))
    print(hotel.salida_huesped(nombre, cedula))

def opcion3():
    print("Situacion actual del Hotel: ")
    hotel.situacion_actual()
hotel = h.Hotel()

opciones = [opcion1, opcion2, opcion3]
opcion = 10
key = True
while key == True:
    opcion = guia()
    if opcion >= 1 and opcion <= 3:
        opciones[opcion - 1]()
    elif opcion == 4:
        key = False
    else:
        print("Opción inválida")