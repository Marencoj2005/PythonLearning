from Tienda import Computador, Tablet
import tkinter as tk

class Metodos_tienda():
    def __init__(self):
        pass
    
    def llenar_inventario(self):
        start = True
        pila_inventario = []
        print("¿Que desea ingresar [C]computadores | [T]tablet ")
        opt = input()
        while start:
            if opt.lower() == "c":
                start2 = True
                while start2:
                    computador_obj = Computador.Computador()
                    print("Ingrese la cantidad de objetos disponibles")
                    # Validar que la cantidad sea un número entero
                    computador_obj.set_cantidad(int(input()))
                    print("Ingrese el precio por unidad")
                    computador_obj.set_precio(float(input()))
                    print("Ingrese el tamaño de su ram")
                    computador_obj.set_tamano_ram(input())
                    print("Ingrese la marca del computador")
                    computador_obj.set_marca(input())
                    print("Ingrese la referencia")
                    computador_obj.set_referencia(input())
                    print("Ingrese el nombre del computador")
                    computador_obj.set_nombre_computador(input())
                    if computador_obj.get_cantidad() < 0:
                        computador_obj.set_disponibilidad(False)
                    else:
                        computador_obj.set_disponibilidad(True)
                    
                    pila_inventario.append(computador_obj) #agrega a la pila
                    
                    print("")
                    print("")
                    print("Desea seguir agregado objeto[S], de lo contrario seleccione [t] para guardar una tablet"
                          "o seleccione [c] para dejar de guardar cualquier objeto")
                    continuar = input()
                    if continuar.lower() == "c":
                        start2 = False
                        start = False
                        return pila_inventario
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
                              
                    pila_inventario.append(table_obj)
                    print("Desea ingresar otro dato? Seleccione [c] si es para una computador, selecciones [s] para continar o [e] para terminar")
                    opt2 = input()
                    if opt2.lower() == "c":
                        opt = opt2
                        start_pila = False
                    elif opt2.lower() == "e":
                        start_pila = False
                        start = False
                        start_pila = False
                        return pila_inventario
            else:
                print("Ingrese una opción válida ")
    
    def buscar(self, pila):
        print("Que desea buscar?")
        print("Computador[c] | Tablet[t] | Cancelar Busqueda[e]")
        opt = str(input())
        if opt.lower() == "c":
            computador_buscado = Computador.Computador()
            print("Ingrese el nombre del computador que desea buscar")
            finding = input()
            for computador_buscado in pila: #tomar el objeto vacio que recorra cada objeto de la pila para mostrarlo u usarlo
                if computador_buscado.get_nombre_computador() == finding:
                    print("Computador encontrado")
                    print("Nombre: ", computador_buscado.get_nombre_computador())
                    print("Marca: ", computador_buscado.get_marca())
                    print("Referencia: ", computador_buscado.get_referencia())
                    print("Precio: ", computador_buscado.get_precio())
                    print("Cantidad: ", computador_buscado.get_cantidad())
                    print("Disponibilidad: ", computador_buscado.get_disponibilidad())
                    print(f"Tamaño RAM : {computador_buscado.get_tamano_ram()}")
                    print("")
        elif opt.lower() == "t":
            print("EN CREACION")
    
    def eliminar():
        pass
    
    def modificar():
        pass
    
    def mostrar(self, pila):
        #aqui procedo a usar GUI para mostrar los resultados 
        #creo el objeto
        ventana = tk.Tk()
        ventana.title("INVENTARIO")
        #Establezco el tamaño
        ventana.geometry("800x600")
        #creo el frame
        frame = tk.Frame(ventana)
        frame.pack()
        #creo el texto
        texto = tk.Text(frame, width=80, height=20)
        texto.pack()
        
    
