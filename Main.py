from Tienda import Metodos_tienda

class Main():
    def __init__(self):
        pass
    
    def main(self):
        metodos_tienda_obj = Metodos_tienda.Metodos_tienda()
        inventario = metodos_tienda_obj.llenar_inventario()
        #inventario = metodos_tienda_obj.mostrar(inventario)
        metodos_tienda_obj.buscar(inventario)

if __name__ == "__main__":
    Main().main()