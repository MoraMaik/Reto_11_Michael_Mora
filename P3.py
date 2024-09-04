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
