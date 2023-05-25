class Cliente:
    def __init__(self, cedula, nombre, habitacion_ocupada):
         self.cedula = cedula
         self.nombre = nombre
         self.habitacion_ocupada = habitacion_ocupada
         
class Hotel:
    def __init__(self, n_habitaciones):
        self.n_habitaciones = n_habitaciones
        self.habitaciones = [True] * n_habitaciones
        self.entradas = {}
        self.salidas = {}
    
            
    def registro(self, cedula, nombre):
        bc = self.buscar_cuartico()
        if bc != None:
            cliente = Cliente(cedula, nombre, bc)
            self.habitaciones[bc] = False
            self.entradas[bc] = cliente
            
    def salida(self, num_habitacion):
        if num_habitacion < self.n_habitaciones:
            if self.habitaciones[num_habitacion] == False:
                
                n = self.entradas.get(num_habitacion)
                self.habitaciones[num_habitacion] = True
                
                if n:
                    self.salidas[num_habitacion] = n
                    del self.entradas[num_habitacion]
                

    def buscar_cuartico(self):
        for i, libre in enumerate(self.habitaciones):
            if libre:
                return i
        return None
    
    def habitaciones_disponibles(self):
        habitacionesfree = []
        for i, libre in enumerate(self.habitaciones):
            if libre:
                habitacionesfree.append(i)
        return habitacionesfree

    def habitaciones_ocupadas(self):
        habitacionesno = []
        for i, libre in enumerate(self.habitaciones):
            if not libre:
                habitacionesno.append(i)
        return habitacionesno
                   
    def info_cliente(self, cedula):
        información = []
        
        for i, cliente in self.entradas.items():
            if cliente.cedula == cedula:
                información.append((i, cliente.nombre))
                
            return información
        
    def info_total(self):
        información = []
        
        for i, cliente in self.entradas.items():
            información.append((i,cliente.nombre))


        return información                

hotelsito = Hotel(5)  # Crear un hotel con 5 habitaciones
hotelsito.registro('1095300441', 'Oscar Carreño')
hotelsito.registro('7817452361', 'Sebastian Badillo')
hotelsito.registro('1234567890', 'Quien sabe')
hotelsito.salida(1)


print("Busqueda cliente:")
print(hotelsito.info_cliente('1095300441'))  


print("\nConsulta de todos los clientes:")
print(hotelsito.info_total())  

print("\nConsulta de habitaciones:")
print("Habitaciones libres:", hotelsito.habitaciones_disponibles()) 
print("Habitaciones ocupadas:", hotelsito.habitaciones_ocupadas())  