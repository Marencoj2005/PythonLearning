"""
Excepciones comunes en Python y cómo solucionarlas:

1. ZeroDivisionError:
    - Ocurre cuando se intenta dividir un número por cero.
    - Solución: Verificar que el divisor no sea cero antes de realizar la operación.
      Ejemplo:
      ```python
      if divisor != 0:
            resultado = dividendo / divisor
      else:
            print("El divisor no puede ser cero.")
      ```

2. IndexError:
    - Ocurre cuando se intenta acceder a un índice que está fuera del rango de una lista o secuencia.
    - Solución: Verificar que el índice esté dentro del rango válido.
      Ejemplo:
      ```python
      if 0 <= indice < len(lista):
            elemento = lista[indice]
      else:
            print("Índice fuera de rango.")
      ```

3. KeyError:
    - Ocurre cuando se intenta acceder a una clave que no existe en un diccionario.
    - Solución: Usar el método `get` del diccionario o verificar si la clave existe antes de acceder a ella.
      Ejemplo:
      ```python
      valor = diccionario.get(clave, "Clave no encontrada")
      ```

4. FileNotFoundError:
    - Ocurre cuando se intenta abrir un archivo que no existe.
    - Solución: Verificar que el archivo exista antes de intentar abrirlo.
      Ejemplo:
      ```python
      if os.path.exists("archivo.txt"):
            with open("archivo.txt", "r") as archivo:
                 contenido = archivo.read()
      else:
            print("El archivo no existe.")
      ```

5. ValueError:
    - Ocurre cuando se pasa un valor inválido a una función o método.
    - Solución: Validar los valores antes de pasarlos a la función.
      Ejemplo:
      ```python
      entrada = input("Introduce un número: ")
      if entrada.isdigit():
            numero = int(entrada)
      else:
            print("Entrada inválida, por favor introduce un número.")
      ```

6. TypeError:
    - Ocurre cuando se realiza una operación en un tipo de dato inapropiado.
    - Solución: Asegurarse de que los tipos de datos sean compatibles antes de realizar la operación.
      Ejemplo:
      ```python
      if isinstance(valor, int) and isinstance(otro_valor, int):
            resultado = valor + otro_valor
      else:
            print("Ambos valores deben ser enteros.")
      ```

7. AttributeError:
    - Ocurre cuando se intenta acceder a un atributo que no existe en un objeto.
    - Solución: Verificar que el objeto tenga el atributo antes de acceder a él.
      Ejemplo:
      ```python
      if hasattr(objeto, "atributo"):
            valor = objeto.atributo
      else:
            print("El objeto no tiene el atributo especificado.")
      ```

Estas son algunas de las excepciones más comunes en Python y cómo manejarlas para evitar que el programa termine abruptamente.

Una excepción en Python es un evento que ocurre durante la ejecución de un programa y que interrumpe el flujo normal del mismo. 
Las excepciones generalmente se producen cuando el programa encuentra un error, como intentar dividir por cero, acceder a un índice fuera de rango en una lista, 
o trabajar con un archivo que no existe. Python proporciona un mecanismo para manejar estas excepciones mediante bloques try-except, 
lo que permite al programador capturar y gestionar errores de manera controlada, evitando que el programa termine abruptamente.
"""

""""""