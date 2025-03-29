class Computador():
    precio = None
    tamano_ram = None
    disponibilidad = None
    marca = None
    nombre_usuario = None
    cantidad = None
    referencia = None
    
    def __init__(self):
        pass
    
    def get_precio(self):
        return self.precio
    def set_precio(self, precio):
        self.precio = precio
    def get_tamano_ram(self):
        return self.tamano_ram
    def set_tamano_ram(self, tamano_ram):
        self.tamano_ram = tamano_ram
        
    def set_referencia(self, referencia):
        self.referencia = referencia
    def get_referencia(self):
        return self.referencia

    def get_disponibilidad(self):
        return self.disponibilidad
    def set_disponibilidad(self, disponibilidad):
        self.disponibilidad = disponibilidad

    def get_marca(self):
        return self.marca
    def set_marca(self, marca):
        self.marca = marca

    def get_nombre_usuario(self):
        return self.nombre_usuario
    def set_nombre_usuario(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario

    def get_cantidad(self):
        return self.cantidad
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad