# declaro y comienzan las listas

matriz = []

filas = []

# declaramos las variables

num_filas = 0

num_columnas = 0

fila = 0

suma_fila = 0.0

def llenar_matriz(matriz, num_filas, num_columnas):
    
    """
    esta funcion llena una matriz con numeros ingresados por el usuario.
    
    Args:
        matriz (list): es una lista que almacenara los elementos de la matriz.
        num_filas (int): representa el numero de filas en la matriz.
        num_columnas (int): representa el numero de columnas en la matriz.
    
    Returns:
        list: la matriz llena como una lista de listas.
    """
    print("Llenando la matriz:")

    for i in range(num_filas):
        fila = []
        for j in range(num_columnas):
            valor = float(input(f"Ingrese el numero para la posicion ({i + 1}, {j + 1}): "))
            fila.append(valor)
        matriz.append(fila)
        print(f"Fila {i + 1}: {' '.join(map(str, fila))}")  # imprime la fila para ver como se construye la matriz

    return matriz

def sumar_fila(matriz, fila):
   
    """
    la funcion suma los elementos de una fila especifica en una matriz.
    
    Args:
        matriz (list): Es una lista de listas que representa la matriz.
        fila (int): Representa el indice de la fila en la matriz que deseas sumar.
    
    Returns:
        float: la suma de los elementos en la fila especificada de la matriz.
    """
    # ajustar el índice de la fila para que sea compatible con el índice de la lista (base 0)
   
    fila -= 1

    # sumar los elementos de la fila especificada
    
    suma_fila = sum(matriz[fila])

    # imprimir la lista de elementos sumados
   
    elementos_fila = matriz[fila]
    print(f"Elementos de la fila {fila + 1} a sumar: {elementos_fila}")
    
    return suma_fila

if __name__ == "__main__":
    
    # solicitar el numero de filas y columnas de la matriz
    
    num_filas = int(input("Ingrese el número de filas: "))
    num_columnas = int(input("Ingrese el número de columnas: "))

    # validar entradas no validas
    if num_filas <= 0 or num_columnas <= 0:

        print("El número de filas y columnas debe ser positivo y mayor a cero.")
    else:
        # llamado de funcion para llenar la matriz
       
        matriz = llenar_matriz(matriz, num_filas, num_columnas)
        
        # solicitar la fila que se desea sumar
       
        fila = int(input("¿Que fila quiere sumar? "))

        # validar que la fila solicitada este dentro del rango de la matriz
       
        if fila < 1 or fila > num_filas:

            print(f"La fila {fila} esta fuera del rango de la matriz.")
        else:

            # llamado de función para sumar la fila

            suma_fila = sumar_fila(matriz, fila)

            print(f"El resultado de la suma es: {suma_fila}")
