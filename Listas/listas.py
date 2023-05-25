# Daniel Sebastian Badillo Neira 2220071
class Nodo:
    # Constructor
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    # Método Ver el valor
    def devolver_valor(self):
        print(self.valor)

    # Método asignar siguiente
    def asignar_siguiente(self, nodo):
        self.siguiente = nodo  # Aqui se genera el

    # Me todo cambiar valor al nodo
    def cambiar_valor(self, nuevo_valor):
        self.valor = nuevo_valor


class Lista:
    # Constructor
    def __init__(self):
        self.primer_nodo = None
        self.tamaño = 0

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        nodo_iterador = self.primer_nodo
        if nodo_iterador == None:
            self.primer_nodo = nuevo_nodo
        else:
            while nodo_iterador.siguiente != None:
                nodo_iterador = nodo_iterador.siguiente
            nodo_iterador.siguiente = nuevo_nodo
        self.tamaño += 1

    def agregar_en_indice(self, valor, indice):
        nuevo_nodo = Nodo(valor)
        index = 0
        nodo_actual = self.primer_nodo
        if indice == 0:
            self.agregar_al_inicio(nuevo_nodo)
        else:
            while nodo_actual != None:
                if (index + 1) == indice:
                    temp = nodo_actual.siguiente
                    nodo_actual.siguiente = nuevo_nodo
                    nuevo_nodo.siguiente = temp
                    self.tamaño += 1
                    return
                else:
                    nodo_actual = nodo_actual.siguiente
                    index += 1

    # agregar al principio
    def agregar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nodo_actual = self.primer_nodo
        if (self.primer_nodo == None):
            self.primer_nodo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = nodo_actual
            self.primer_nodo = nuevo_nodo
        self.tamaño += 1

    def agregar_despues_de(self, valor_agregar, valor_guia):
        nuevo_nodo = Nodo(valor_agregar)
        nodo_actual = self.primer_nodo

        while nodo_actual != None:
            if nodo_actual.valor == valor_guia:
                nodo_temp = nodo_actual.siguiente
                nodo_actual.siguiente = nuevo_nodo
                nuevo_nodo.siguiente = nodo_temp
                self.tamaño += 1
                return False
            else:
                nodo_actual = nodo_actual.siguiente

    def buscar(self, valor):
        key = False
        nodo_actual = self.primer_nodo
        while nodo_actual != None:
            if (nodo_actual.valor == valor):
                key = True
                return nodo_actual
            else:
                nodo_actual = nodo_actual.siguiente
        if (key == False):
            return 'Not found'

    def eleminar_ultimo(self):
        nodo_actual = self.primer_nodo
        nodo_anterior = None
        while nodo_actual.siguiente != None:
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
        nodo_anterior.siguiente = None
        self.tamaño -= 1

    def eliminar_por_indice(self, posicion):
        if posicion < self.tamaño:
            indice = 0
            nodo_actual = self.primer_nodo
            while nodo_actual != None:
                if (indice == posicion):
                    self.eliminar(nodo_actual.valor)
                    self.tamaño -= 1
                    return True
                else:
                    nodo_actual = nodo_actual.siguiente
                    indice += 1

    def contar_veces(self, valor):
        nodo_actual = self.primer_nodo
        veces = 0
        while nodo_actual != None:
            if (nodo_actual.valor == valor):
                veces += 1
                nodo_actual = nodo_actual.siguiente
            else:
                nodo_actual = nodo_actual.siguiente
        if (veces == 0):
            return "El numero no se encuentra en la lista"
        else:
            return veces

    def eliminar(self, valor):
        nodo_actual = self.primer_nodo
        nodo_anterior = None
        while nodo_actual != None:
            if (nodo_actual.valor == valor):
                if (nodo_anterior == None):
                    self.primer_nodo = nodo_actual.siguiente
                    nodo_actual = nodo_actual.siguiente
                else:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                    nodo_actual = nodo_actual.siguiente
                self.tamaño -= 1
                return
            else:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente

    def encontrar_posiciones(self, valor):
        posicion = 0
        posiciones = []
        key = False
        nodo_actual = self.primer_nodo
        while nodo_actual != None:
            if (nodo_actual.valor == valor):
                key = True
                posiciones.append(posicion)
                nodo_actual = nodo_actual.siguiente
            else:
                nodo_actual = nodo_actual.siguiente
            posicion += 1
        if key == False:
            return 'El elemento no se encuentra en la lista'
        else:
            return posiciones

    def __str__(self):
        nodos = []
        nodo_iterador = self.primer_nodo
        while nodo_iterador != None:
            nodos.append(str(nodo_iterador.valor))
            nodo_iterador = nodo_iterador.siguiente
        return '[' + ', '.join(nodos) + ']'
lista = Lista()
lista.agregar_al_final(2)
lista.agregar_al_final(2)
lista.agregar_al_final(2)
lista.agregar_al_final(2)
lista.agregar_al_final(2)
lista.agregar_al_final(2)
lista.agregar_despues_de(6,2)
lista.agregar_en_indice(6,3)
print(lista)
lista.eleminar_ultimo()
print(lista)