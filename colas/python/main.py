class main_class():
    def main(self):
        cola = []
        bandera = True
        mensaje = """Bienvenido al carrito Perros llaneros,
        Seleccione nuestro menú:
        [1] Perro caliente
        [2] Perra
        [3] Hamburguesas
        [4] No gracias"""
        while bandera:
            
            option = int(input("¿Desea ingresar registro? [1]Si | [2]No\n "))
            if option == 2:
                print("Gracias por su visita")
                bandera = False
                
            print(mensaje) #muestra el menu
            selection = int(input()) #Ingresa los datos en funcion al funcion
            
            """Valida los datos"""
            while type(option) != int:
                print("Selección incorrecta")
                option = int(input("¿Desea ingresar registro? [1]Si | [2]No\n "))
            while option > 4 or option < 1:
                print("Pagina en mantenimiento")
                option = int(input("¿Desea ingresar registro? [1]Si | [2]No\n "))
            
            #si es correcto option, entonces, pase a los if
            if selection == 1:
                print("En mantenimiento")
                break
            elif selection == 2:
                print("En mantenimiento")
                break
            elif selection == 3:
                print("En mantenimiento")
                break
            else:
                print("Gracias por su visita")
                bandera = False

        
if __name__ == "__main__":
    main_class().main()