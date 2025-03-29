from Tienda import Computador, Tablet

class Metodos_tienda():
    def __init__(self):
        pass
    
    def llenar_inventario(self):
        start = True
        pila_pc = []
        pila_tablet = []
        while start:
            print("¿Que desea ingresar [C]computadores | [T]tablet ")
            opt = input()
            if opt.lower() == "c":
                start2 = True
                while start2:
                    computador_obj = Computador.Computador()
                    print("Ingrese la cantidad de objetos")
                    computador_obj.set_cantidad(input())
                    print("Ingrese el precio por unidad")
                    computador_obj.set_precio(input())
                    print("Ingrese el tamaño de su ram")
                    computador_obj.set_tamano_ram(input())
                    print("Ingrese la marca del computador")
                    computador_obj.set_marca(input())
                    print("Ingrese la referencia")
                    computador_obj.set_referencia(input())
                    if computador_obj.get_cantidad() < 0:
                        computador_obj.set_disponibilidad(False)
                    else:
                        computador_obj.set_disponibilidad(True)
                    pila_pc.append(computador_obj) #agrega a la pila
                    
                    print("")
                    print("")
                    print("Desea seguir agregado objeto[S], de lo contrario seleccione [t] para guardar una tablet"
                          "o seleccione [c] para dejar de guardar")
                    continuar = input()
                    if continuar.lower() == "c":
                        start2 = False
                        start = False
                    elif continuar.lower() == "t":
                        opt = "t"
                        start2 = False
            elif opt.lower() == "t":
                start_pila = True
                while start_pila:
                    table_obj = Tablet.Tablet()
                    print("Ingrese el precio por unidad ")
                    table_obj.set_precio(float(input()))
                    print("Ingrese la marca")
                    table_obj.set_marca(input())
                    print("Ingrese la referencia")
                    table_obj.set_referencia(input())
                    print("Ingrese la cantidad de ejemplares disponibles")
                    table_obj.set_cantidad(int(input()))                    
                pass
            else:
                print("Ingrese una opción válida ")
