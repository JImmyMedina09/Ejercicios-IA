def crear_matriz():
    # Inicializar una matriz 6x6 llena de ceros
    matriz = [[0 for _ in range(6)] for _ in range(6)]
    
    # Rellenar con unos la parte correspondiente
    for i in range(1, 6):
        for j in range(i):
            matriz[i][j] = 1
    
    # Imprimir la matriz
    for fila in matriz:
        print(fila)

# Llamar a la función para crear e imprimir la matriz
crear_matriz()
