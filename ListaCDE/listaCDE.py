#Lista circular Doblemente Enlazada
class Nodo:
    def __init__(self, dato , siguiente, anterior):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

class Lista:
    def __init__(self, primer_nodo, ultimo_nodo):
        self.primer_nodo = Nodo(primer_nodo,'','')
        self.ultimo_nodo = Nodo(ultimo_nodo, self.primer_nodo,self.primer_nodo)
        self.primer_nodo.siguiente = self.ultimo_nodo# type: ignore
        self.primer_nodo.anterior = self.ultimo_nodo# type: ignore
        self.lenght = 2
    
    #Agregar al inicio
    def agregar_inicio(self, dato ):
        nuevo_nodo = Nodo(dato, self.primer_nodo, self.ultimo_nodo)
        self.ultimo_nodo.siguiente = nuevo_nodo # type: ignore
        self.primer_nodo.anterior = nuevo_nodo# type: ignore
        self.primer_nodo = nuevo_nodo
        self.lenght +=1
    
    # Agregar al final
    def agregar_final(self, dato ):
        nuevo_nodo = Nodo(dato, self.primer_nodo, self.ultimo_nodo)
        self.primer_nodo.anterior = nuevo_nodo # type: ignore
        self.ultimo_nodo.siguiente = nuevo_nodo # type: ignore
        self.ultimo_nodo = nuevo_nodo
        self.lenght +=1

    def agregar_indice(self, data, indice):
        nodo_guia = self.primer_nodo
        if (indice ==0 ):
            self.agregar_inicio(data)
        else: 
            index = 0
            for x in range (0,self.lenght):
                if index == indice:
                    nuevo_nodo = Nodo(data, nodo_guia, nodo_guia.anterior)# type: ignore
                    nodo_guia.anterior.siguiente = nuevo_nodo# type: ignore
                    nodo_guia.anterior = nuevo_nodo# type: ignore
                    if index == (self.lenght-1):
                        self.ultimo_nodo = nodo_guia
                    self.lenght +=1
                nodo_guia = nodo_guia.siguiente# type: ignore
                index +=1
                





    # Eliminar Nodo
    def elimiminar_nodo(self, dato):
        nodo_actual = self.primer_nodo
        if self.primer_nodo.dato == dato:# type: ignore
            self.ultimo_nodo.siguiente = self.primer_nodo.siguiente# type: ignore
            self.primer_nodo.siguiente.anterior = self.ultimo_nodo# type: ignore
            self.primer_nodo = self.primer_nodo.siguiente
            self.lenght -=1
            return 0
        elif self.ultimo_nodo == dato:
            self.ultimo_nodo.anterior.siguiente = self.primer_nodo# type: ignore
            self.primer_nodo.anterior = self.ultimo_nodo.anterior# type: ignore
            self.ultimo_nodo = self.ultimo_nodo.anterior# type: ignore
            self.lenght -=1
            return 0
        else:
            for x in range(0, self.lenght):
                if nodo_actual.dato == dato:# type: ignore
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente# type: ignore
                    nodo_actual.siguiente.anterior = nodo_actual.anterior# type: ignore
                    self.lenght -=1
                    return 0
                else:
                    nodo_actual = nodo_actual.siguiente# type: ignore
                
                    

    def __str__(self):
        nodos = []
        nodo_iterador = self.primer_nodo
        for x in range(0, self.lenght):
            nodos.append(str(nodo_iterador.dato))# type: ignore
            print(nodo_iterador)
            nodo_iterador = nodo_iterador.siguiente# type: ignore
        #print(nodo_iterador)
        #nodos.append(str(self.ultimo_nodo.dato))# type: ignore
        return '[' + ', '.join(nodos) + ']'
    
    def recorrer(self):
        nodos = []
        nodo_iterador = self.primer_nodo
        for x in range(0, self.lenght):
            nodos.append(str(nodo_iterador.dato))# type: ignore
            
            nodo_iterador = nodo_iterador.siguiente# type: ignore
        return '[' + ', '.join(nodos) + ']'
    
    def recorrer_reversa(self):
        nodos = []
        nodo_iterador = self.ultimo_nodo
        for x in range(0, self.lenght):
            nodos.append(str(nodo_iterador.dato))# type: ignore
            
            nodo_iterador = nodo_iterador.anterior# type: ignore
        return '[' + ', '.join(nodos) + ']'


lista = Lista(2,4)
lista.agregar_inicio(1)
lista.agregar_final(2)
lista.agregar_final(79)
#lista.elimiminar_nodo(2)
lista.agregar_indice(2,4)

print(lista)
print(lista.ultimo_nodo)
print(lista.ultimo_nodo.dato)# type: ignore
print(lista.lenght)
print(lista.recorrer())
print(lista.recorrer_reversa())