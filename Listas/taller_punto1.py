import Listas.listas as li

def opciones():
    print("""
        1. Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
        2. Añadir número de la lista en una posición: Me pide un número y una posición, 
            y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
        3. Longitud de la li1sta: te muestra el número de elementos de la lista.
        4. Eliminar el último número: Muestra el último número de la lista y lo borra.
        5. Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
        6. Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
        7. Posiciones de un número: Te pide un número y te dice en qué posiciones está (contando desde 1).
        8. Mostrar números: Muestra los números de la lista
        9. Salir
    """)
    respuesta = int(input("¿ Que desea realizar el dia de hoy ? [Digite un numero entre 1 y 9] "))
    return respuesta

rta = 1
lista = li.Lista()
while rta != 9: 

    rta = opciones()
    

    if rta == 1:
        print("Vamos a añadir un numero al final ")
        numero = int(input("Ingrese un número por favor "))
        if not isinstance(numero,int):
            numero = int(input("Ingrese un número por favor "))
        lista.agregar_al_final(numero)
        print(lista)
        
    elif rta == 2:
        print("Vamos a añadir un numero en una posicion especifica ")
        numero = int(input("Ingrese un número por favor "))
        posicion = int(input("¿ En que posición desea agregar el numero "))

        if not isinstance(numero,int) :
            numero = int(input("Ingrese un número por favor "))

        if  not isinstance(posicion,int):
            posicion = int(input("¿ En que posición desea agregar el numero "))

        if posicion >= lista.tamaño:
            posicion = int(input("Ingrese una nueva posicion, la posicion suministrada no se encuentra en la lista "))
        pos = posicion-1
        lista.agregar_en_indice(numero, posicion)
        print(lista)
        
    elif rta == 3 :
        print("El tamaño de la lista es: ")
        print(lista.tamaño)
        print(lista)
        

    elif rta ==4:
        print("Vamos a eliminar el ultimo numero de la lista ")
        lista.eleminar_ultimo()
        print(lista)
        

    elif rta ==5:
        print("Vamos a eliminar")
        indice = int(input("Porfavor ingrese el indice que desea eliminar: "))
        while indice >= lista.tamaño: 
            indice = int(input("Porfavor ingrese el indice que desea eliminar: "))
        lista.eliminar_por_indice(indice)
        print(lista)
        

    elif rta == 6:
        numero = int(input(" Vamos a contar las veces que aparece el numero: "))
        print(lista.contar_veces(numero))
        print(lista)
        
    elif rta == 7:
        numero = int(input(" Vamos a encontrar las posiciones del numero:  "))
        print(lista.encontrar_posiciones(numero))
        print(lista)
        
    elif rta == 8:
        print(lista)
        