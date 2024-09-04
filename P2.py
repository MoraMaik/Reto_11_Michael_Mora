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
