class Hotel:
    def __init__(self):
        self.rooms = {}
        self.check_ins = {}
        self.check_outs = {}

    def check_in(self, cedula, nombre, numero_habitacion):
        self.rooms[numero_habitacion] = (cedula, nombre)
        self.check_ins[cedula] = (nombre, numero_habitacion)

    def check_out(self, cedula):
        if cedula in self.check_ins:
            _, numero_habitacion = self.check_ins[cedula]
            del self.check_ins[cedula]
            del self.rooms[numero_habitacion]
            self.check_outs[cedula] = numero_habitacion

    def get_guest_info(self, cedula):
        if cedula in self.check_ins:
            nombre, numero_habitacion = self.check_ins[cedula]
            return f"Cédula: {cedula}\nNombre: {nombre}\nHabitación: {numero_habitacion}"
        elif cedula in self.check_outs:
            numero_habitacion = self.check_outs[cedula]
            return f"Cédula: {cedula}\nNombre: [Check-out]\nHabitación: {numero_habitacion}"
        else:
            return "No se encontró información para el huésped especificado."

    def get_all_guests_info(self, order_by="cedula"):
        if order_by == "cedula":
            sorted_guests = sorted(self.check_ins.items(), key=lambda x: x[0])
        elif order_by == "llegada":
            sorted_guests = sorted(self.check_ins.items(), key=lambda x: x[1][1])
        else:
            return "Orden no válido. Debe ser 'cedula' o 'llegada'."

        guests_info = []
        for cedula, (nombre, numero_habitacion) in sorted_guests:
            guests_info.append(f"Cédula: {cedula}\nNombre: {nombre}\nHabitación: {numero_habitacion}")

        return "\n".join(guests_info)

    def get_available_rooms(self):
        all_rooms = set(range(1, 101))
        occupied_rooms = set(self.rooms.keys())
        available_rooms = all_rooms - occupied_rooms
        return sorted(available_rooms)

    def get_occupied_rooms(self):
        return sorted(self.rooms.keys())


# Ejemplo de uso:
hotel = Hotel()

# Check-in de huéspedes
hotel.check_in("123456789", "Juan Pérez", 101)
hotel.check_in("987654321", "María Gómez", 203)
hotel.check_in("456789123", "Pedro Sánchez", 305)

# Check-out de un huésped
hotel.check_out("987654321")

# Obtener información de un huésped específico
print(hotel.get_guest_info("123456789"))

# Obtener información de todos los huéspedes ordenados por cédula
print(hotel.get_all_guests_info(order_by="cedula"))

# Obtener información de todos los huéspedes ordenados por orden de llegada
print(hotel.get_all_guests_info(order_by="llegada"))

# Obtener lista de habitaciones disponibles
print(hotel.get_available_rooms())


