class Node:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = Lista()

    def agregar_hijo(self,hijo):
        self.hijos.agregar(hijo)

class Nodo:
    def __init__(self, dato):
        self.dato = Node(dato)
        self.siguiente = None

class Lista:
    def __init__(self):
        self.primero = None
        self.size = 0

    def agregar(self, dato):
        if self.primero == None:
            self.primero = Nodo(dato)
            self.size+= 1
        else:
            nodo_iterador = self.primero
            while nodo_iterador.siguiente != None:
                nodo_iterador = nodo_iterador.siguiente
            nodo_iterador.siguiente = Nodo(dato)
            self.size += 1

    def getSize(self):
        return self.size

    def __getitem__(self, index):
        current = self.primero
        for x in range(index):
            if current is None:
                raise IndexError("Índice fuera de rango")
            current = current.siguiente
        if current is None:
            raise IndexError("Índice fuera de rango")
        return current.dato

    def __str__(self):

        nodos = ''
        nodo_iterador = self.primero
        while nodo_iterador != None:
            nodos += f'{nodo_iterador.dato.dato}, '
            nodo_iterador = nodo_iterador.siguiente
        nodos += ' ]'
        return nodos


class Tree:
    def __init__(self):
        self.root = None
        self.peso = 0

    def agregar_nodo(self, padre, valor):
        if self.root == None:
            self.root = Node(valor)
        else:
            # self.root.hijos.agregar(valor)
            papa = self.recorredor(self.root, padre)
            papa.hijos.agregar(valor)


    def recorredor(self, nodo, padre):
        if nodo.dato == padre:
            return nodo
        contador = nodo.hijos.size
        for x in range (0, contador):
            nod = nodo.hijos[x]
        
            if nod.dato == padre:
                return nod
            else:
                if nod.hijos.size != 0:
                    result = self.recorredor(nod, padre)
                    if result is not None:
                        return result
        return None

    def imprimir(self, nodo, primeravez=True, nivel=2):
        if primeravez:
            print(f'Root: {self.root.dato}')
        nodo1  = nodo
        contador = nodo1.hijos.size
        
        for x in range (0, contador):
            nod = nodo1.hijos[x]
            print(f'Nivel {nivel}: {nod.dato}')

            if nod.hijos.size != 0:
                self.imprimir(nod, primeravez=False, nivel= nivel+1)

    def calcPeso(self, nodo, primeravez=True, peso =0):
        if primeravez:
            if nodo != None:
                peso +=1

        contador = nodo.hijos.size
        for x in range (0, contador):
            nod = nodo.hijos[x]
            peso += 1
            
            if nod.hijos.size != 0:
                nuevo = self.calcPeso(nod,primeravez=False,peso = peso)
                peso = nuevo
        return peso
                    
    def calcAltura(self, nodo,  primeravez=True, nivel=2):
        
        nodo1  = nodo
        contador = nodo1.hijos.size
        for x in range (0, contador):
            nod = nodo1.hijos[x]
            if nod.hijos.size != 0:
                nivel = self.calcAltura(nod, primeravez=False, nivel= nivel+1)
        return nivel

    def calcOrden(self, nodo, maximo = 0):
        orden = 0
        contador = nodo.hijos.size
        
        for x in range (0, contador):
            nod = nodo.hijos[x]
            orden = nodo.hijos.size
            if orden >= maximo:
                    maximo = orden
            if nod.hijos.size != 0:
                orden = self.calcOrden(nod)
                if orden >= maximo:
                    maximo = orden
        return maximo


yo = Tree()
yo.agregar_nodo(0, 10)
yo.agregar_nodo(10, 12)
yo.agregar_nodo(12, 14)
yo.agregar_nodo(10, 2)
yo.agregar_nodo(14, 1)
yo.agregar_nodo(1, 17)
yo.agregar_nodo(1, 18)
yo.agregar_nodo(1, 19)
yo.agregar_nodo(1, 20)
yo.agregar_nodo(1, 27)
yo.agregar_nodo(10, 40)
# yo.agregar_nodo(12, 16)
# yo.agregar_nodo(16, 100)
# yo.agregar_nodo(12, 18)
#

# print(yo.root.hijos.size)
# # print(yo.root.hijos[2].dato)
# print(yo.root.hijos[1].hijos.size)


yo.imprimir(yo.root)
print(yo.calcPeso(yo.root))
print(yo.calcAltura(yo.root))
print(yo.calcOrden(yo.root))