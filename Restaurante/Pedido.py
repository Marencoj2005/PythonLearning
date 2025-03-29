#clase donde se crean los pedidos (objetos)
class Pedido():
    id_pedido = None 
    cantidad = None
    precio = None
    total_pedidos = None
    precio_total = None
    
    
    def __init__(self):
        pass
    
    # Setter y Getter para id_pedido
    def set_id_pedido(self, id_pedido):
        self.id_pedido = id_pedido
    def get_id_pedido(self):
        return self.id_pedido
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    def get_cantidad(self):
        return self.cantidad
    def set_precio(self, precio):
        self.precio = precio
    def get_precio(self):
        return self.precio
    def set_total_pedidos(self, total_pedidos):
        self.total_pedidos = total_pedidos
    def get_total_pedidos(self):
        return self.total_pedidos
    def set_precio_total(self, precio_total):
        self.precio_total = precio_total
    def get_precio_total(self):
        return self.precio_total
    