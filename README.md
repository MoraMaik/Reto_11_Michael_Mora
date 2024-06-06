# Reto_11_Michael_Mora
Desarrollo reto 11, según lo aprendido en clase con Matrices.

*(Al final de cada codigo dejo una breve explicacion si miro que es necesario)*

_______________________________
## **Punto 1**

**Instrucciones:** Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.


```python

# se declaran e inicializan las listas

matriz_primera = []

matriz_segunda = []

matriz_suma = []

matriz_resta = []

filas = []

# declaro las variables

num_filas_primera = 0

num_columnas_primera = 0

num_filas_segunda = 0

num_columnas_segunda = 0

def llenar_matriz(matriz, num_filas, num_columnas, nombre):

    """
    Esta función llena una matriz con valores ingresados por el usuario.

    Args:
        matriz (list): la matriz que sera llenada.
        num_filas (int): el numero de filas de la matriz.
        num_columnas (int): el numero de columnas de la matriz.
        nombre (str): el nombre de la matriz para los mensajes al usuario.

    Returns:
        list: La matriz llena con los valores ingresados por el usuario.
    """

    print(f"Llenando la {nombre} matriz:")

    for i in range(num_filas):
        filas = []
        for j in range(num_columnas):
            valor = float(input(f"{nombre} matriz: ingrese el número ({i + 1}, {j + 1}): "))
            filas.append(valor)
        matriz.append(filas)

        print(f"[{' '.join(map(str, filas))}]")  # Imprime la fila para ver cómo se construye la matriz

    return matriz

def sumar_matrices(matriz_primera, matriz_segunda):

    """
    Esta funcion suma dos matrices y devuelve la matriz resultante.

    Args:
        matriz_primera (list): la primera matriz.
        matriz_segunda (list): la segunda matriz.

    Returns:
        list: La matriz resultante de la suma de las dos matrices.
    """

    matriz_suma = []
    for i in range(len(matriz_primera)):
        filas = []
        for j in range(len(matriz_primera[0])):
            filas.append(matriz_primera[i][j] + matriz_segunda[i][j])
        matriz_suma.append(filas)

        print(filas)        # imprime la fila para ver cómo se construye la matriz

    return matriz_suma

def restar_matrices(matriz_primera, matriz_segunda):
    """
    Esta función resta dos matrices y devuelve la matriz resultante.

    Args:
        matriz_primera (list): La primera matriz.
        matriz_segunda (list): La segunda matriz.

    Returns:
        list: La matriz resultante de la resta de las dos matrices.
    """
    matriz_resta = []
    for i in range(len(matriz_primera)):
        filas = []
        for j in range(len(matriz_primera[0])):
            filas.append(matriz_primera[i][j] - matriz_segunda[i][j])
        matriz_resta.append(filas)
        print(filas)  # Imprime la fila para ver cómo se construye la matriz

    return matriz_resta

if __name__ == "__main__":

    # solicitar el numero de filas y columnas de la primera matriz

    num_filas_primera = int(input("Primera matriz: ingrese número de filas: "))
    num_columnas_primera = int(input("Primera matriz: ingrese número de columnas: "))

    # solicitar el número de filas y columnas de la segunda matriz

    num_filas_segunda = int(input("Segunda matriz: ingrese número de filas: "))
    num_columnas_segunda = int(input("Segunda matriz: ingrese número de columnas: "))

    # validar si las matrices tienen el mismo tamaño para poder sumarlas o restarlas

    if num_filas_primera != num_filas_segunda or num_columnas_primera != num_columnas_segunda:
        print("No se pueden sumar o restar las matrices porque no tienen el mismo tamaño.")
    else:
        # llenar la primera matriz con los valores ingresados por el usuario
        matriz_primera = llenar_matriz(matriz_primera, num_filas_primera, num_columnas_primera, "Primera")

        # llenar la segunda matriz con los valores ingresados por el usuario
        matriz_segunda = llenar_matriz(matriz_segunda, num_filas_segunda, num_columnas_segunda, "Segunda")

        # sumar las dos matrices

        print("La suma de las matrices es:")
        matriz_suma = sumar_matrices(matriz_primera, matriz_segunda)

        # restar las dos matrices

        print("La resta de las matrices es:")
        matriz_resta = restar_matrices(matriz_primera, matriz_segunda)

```
_______________________________

## **Punto 2**

**Instrucciones:** Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.


```python

**Instrucciones:** Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
# declaran e inicializan las listas

matriz_primera = []

matriz_segunda = []

matriz_final = []

multiplicacion_final = []

filas = []

# declaran las variables

num_filas_primera = 0

num_columnas_primera = 0

num_filas_segunda = 0

num_columnas_segunda = 0

producto_elemento = 0.0

def llenar_matriz(matriz, num_filas, num_columnas, nombre):
    
    """
    esta funcion llena una matriz con valores ingresados por el usuario fila por fila y muestra la matriz a medida que se construye.
    
    Args:
        matriz (list): es una lista que almacenara los valores de la matriz que el usuario ingresara.
        num_filas (int): representa el numero de filas de la matriz.
        num_columnas (int): el parametro representa el numero de columnas de la matriz.
        nombre (str): el nombre de la matriz para los mensajes al usuario.
    
    Returns:
        list: La matriz llena con los valores ingresados por el usuario.
    """

    print(f"Llenando la {nombre} matriz:")

    for i in range(num_filas):
        filas = []
        for j in range(num_columnas):
            valor = float(input(f"{nombre} matriz: ingrese el numero ({i + 1}, {j + 1}): "))
            filas.append(valor)
        matriz.append(filas)

        print(f"[{' '.join(map(str, filas))}]")  # imprime la fila para ver camo se construye la matriz

    return matriz

def multiplicar_matrices(matriz_primera, matriz_segunda):
    
    """
    La función toma dos matrices como entrada, las multiplica y devuelve la matriz resultante.
    
    Args:
        matriz_primera (list): representa la primera matriz que se desea multiplicar con la segunda matriz.
        matriz_segunda (list): representa la segunda matriz que se desea multiplicar con la primera matriz.
    
    Returns:
        list: la matriz resultante de la multiplicacion de las dos matrices.
    """
    
    multiplicacion_final = []

    # recorren las filas de la primera matriz

    for i in range(len(matriz_primera)):
        fila_resultante = []

        # recorren las columnas de la segunda matriz

        for j in range(len(matriz_segunda[0])):

            # calcular el producto escalar de la fila de matriz_primera con la columna de matriz_segunda

            producto_elemento = 0
            for k in range(len(matriz_primera[0])):
                producto_elemento += matriz_primera[i][k] * matriz_segunda[k][j]
            fila_resultante.append(producto_elemento)
        multiplicacion_final.append(fila_resultante)
        print(fila_resultante)  # imprime la fila para ver como se construye la matriz

    return multiplicacion_final

if __name__ == "__main__":

    # wolicitar el numero de filas y columnas de la primera matriz

    num_filas_primera = int(input("Primera matriz: ingrese numero de filas: "))
    num_columnas_primera = int(input("Primera matriz: ingrese número de columnas: "))

    # solicitar el numero de filas y columnas de la segunda matriz

    num_filas_segunda = int(input("Segunda matriz: ingrese numero de filas: "))
    num_columnas_segunda = int(input("Segunda matriz: ingrese numero de columnas: "))

    # validar si se pueden multiplicar las matrices (el numero de columnas de la primera debe ser igual al numero de filas de la segunda)
   
    if num_columnas_primera != num_filas_segunda:
        print("No se pueden multiplicar las matrices porque el numero de columnas de la primera es diferente al numero de filas de la segunda.")
    else:
        # llenar la primera matriz con los valores ingresados por el usuario
        matriz_primera = llenar_matriz(matriz_primera, num_filas_primera, num_columnas_primera, "Primera")

        # llenar la segunda matriz con los valores ingresados por el usuario
        matriz_segunda = llenar_matriz(matriz_segunda, num_filas_segunda, num_columnas_segunda, "Segunda")

        # multiplicar las dos matrices
        print("La multiplicacion de las matrices es:")
        matriz_final = multiplicar_matrices(matriz_primera, matriz_segunda)
```
_______________________________

## **Punto 3**

**Instrucciones:** Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.


```python
# declaro e inicializo las listas
matriz = []

matriz_traspuesta = []

filas = []

# dclaro las variables
num_filas = 0

num_columnas = 0

def llenar_matriz(matriz, num_filas, num_columnas, filas):
   
    """
    la función `llenar_matriz` toma una lista que representa una matriz y la llena con los parametros ingresados por el usuario y devuelve la matriz completa.
    
    Args:
        matriz (list): es una lista que almacenara los elementos de la matriz que se va a llenar.
        num_filas (int): representa el numero de filas en la matriz que el usuario desea crear.
        num_columnas (int): representa el número de columnas en la matriz que el usuario desea crear.
        filas (list): es una lista que se usa para almacenar los numeros que el usuario ingresa para cada fila de la matriz. 
    
    Returns:
        list: Se devuelve la matriz llena como una lista de listas despues de que el usuario haya ingresado los numeros para cada celda de la matriz.
    """

    print(f"La matriz se ve de la siguiente forma:")

    for i in range(num_filas):
        filas = []
        for j in range(num_columnas):
            valor = float(input(f"Ingrese el numero ({i + 1}, {j + 1}): "))
            filas.append(valor)
        matriz.append(filas)
        print(f"[{' '.join(map(str, filas))}]")  # imprime la fila para ver cómo se construye la matriz

    return matriz

def trasponer_matriz(matriz, num_filas, num_columnas):
    
    """
    esta funcion transpone una matriz segun el numero de filas y columnas proporcionadas.
    
    Args:
        matriz (list): es la matriz original que se va a trasponer.
        num_filas (int): representa el numero de filas en la matriz original.
        num_columnas (int): representa el numero de columnas en la matriz original.
    
    Returns:
        list: se devuelve una matriz transpuesta basada en los parametros de entrada y la matriz proporcionada.
    """
    
    matriz_traspuesta = []

    print(f"la matriz traspuesta se ve de la siguiente forma:")

    for i in range(num_columnas):
        filas = []
        for j in range(num_filas):
            filas.append(matriz[j][i])
        matriz_traspuesta.append(filas)
        print(f"[{' '.join(map(str, filas))}]")  # imprime la fila para ver como se construye la matriz transpuesta

    return matriz_traspuesta

if __name__ == "__main__":
    
    # solicitar el numero de filas y columnas de la matriz
   
    num_filas = int(input("Ingrese número de filas: "))
    num_columnas = int(input("Ingrese número de columnas: "))

    # validar entradas no validas
   
    if num_filas == 0 and num_columnas == 0:
        print("La matriz no tiene filas ni columnas :(")
    elif num_filas < 0 or num_columnas < 0:
        print("Una cantidad negativa de columnas/filas no es permitida")
    else:
       
        # llamado de funcion para llenar la matriz
       
        matriz = llenar_matriz(matriz, num_filas, num_columnas, filas)
        
        # llamado de funcion para trasponer la matriz
       
        matriz_traspuesta = trasponer_matriz(matriz, num_filas, num_columnas)
```
_______________________________

## **Punto 4**

**Instrucciones:** Desarrollar un programa que sume los elementos de una columna dada de una matriz.


```python


