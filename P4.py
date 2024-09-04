# declaramos y comienzan las listas

matriz = []

filas = []

# declaramos las variables

num_filas = 0

num_columnas = 0

columna = 0

suma_columna = 0.0

def llenar_matriz(matriz, num_filas, num_columnas, filas):
    
    """
    esta funcion de Python llena una matriz con numeros ingresados por el usuario.
    
    Args:
        matriz (list): es una lista que almacenara los elementos de la matriz que se está llenando.
        num_filas (int): representa el numero de filas en la matriz que el usuario quiere crear.
        num_columnas (int): representa el numero de columnas en la matriz que el usuario desea crear.
        filas (list): es una lista que se utiliza para almacenar los elementos de cada fila de la matriz. 
    
    Returns:
        list: se devuelve la matriz llena como una lista.
    """
    print(f"La matriz se ve de la siguiente forma:")

    for i in range(num_filas):
        filas = []
        for j in range(num_columnas):
            valor = float(input(f"Ingrese el numero ({i + 1}, {j + 1}): "))
            filas.append(valor)
        matriz.append(filas)
        print(f"[{' '.join(map(str, filas))}]")  # imprime la fila para ver como se construye la matriz

    return matriz

def sumar_columnas(matriz, columna):
    """
    la funcion `sumar_columnas` toma una matriz y un indice de columna como entrada, suma los elementos de esa columna y devuelve la suma.
    
    Args:
        matriz (list): es una lista de listas que representa la matriz.
        columna (int): representa el indice de la columna en la matriz que desea sumar.
    
    Returns:
        float: se devuelve la suma de los elementos en la columna especificada de la matriz de entrada.
    """
    # ajustar el indice de la columna para que sea compatible con el indice de la lista (base 0)
    columna -= 1

    # sumar los elementos de la columna especificada
   
    suma_columna = sum(matriz[i][columna] for i in range(len(matriz)))

    # imprimir la lista de elementos sumados
    
    elementos_columna = [matriz[i][columna] for i in range(len(matriz))]
    print(f"Columna a sumar: {elementos_columna}")
    
    return suma_columna

if __name__ == "__main__":
    
    # solicitar el numero de filas y columnas de la matriz
    
    num_filas = int(input("Ingrese numero de filas: "))
    num_columnas = int(input("Ingrese numero de columnas: "))

    
    # validar entradas no validas
    
    if num_filas == 0 and num_columnas == 0:
        
        print("La matriz no tiene filas ni columnas :(")
    elif num_filas < 0 or num_columnas < 0:
        
        print("Una cantidad negativa de columnas/filas no es permitida")
    else:
       
        # llamado de funcion para llenar la matriz

        matriz = llenar_matriz(matriz, num_filas, num_columnas, filas)

        # solicitar la columna que se desea sumar

        columna = int(input("¿Qué columna quiere sumar? "))

        # validar que la columna solicitada este dentro del rango de la matriz

        if columna < 1 or columna > num_columnas:
            print(f"La columna {columna} esta fuera del rango de la matriz.")
        else:

            # llamado de funcion para sumar la columna

            suma_columna = sumar_columnas(matriz, columna)

            print(f"el resultado de la suma es: {suma_columna}")
