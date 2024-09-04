
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
