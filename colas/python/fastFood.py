class fastFood():
    id_orden = None
    orden = None
    precio = None
    cantidad = None
    
    def __init__(self):
        pass
    """puedo crear un constructor con objetos, debo averiguar eso"""
    
    def set_id_orden(self, id_orden):
        self.id_orden = id_orden
    
    def get_id_orden(self):
        return self.id_orden

    # Setter y Getter para orden
    def set_orden(self, orden):
        self.orden = orden

    def get_orden(self):
        return self.orden
    
     # Setter y Getter para precio
    def set_precio(self, precio):
        self.precio = precio

    def get_precio(self):
        return self.precio

    # Setter y Getter para cantidad
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad