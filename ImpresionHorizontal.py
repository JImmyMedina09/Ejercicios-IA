def imprimir_impares_inverso(inicio, fin):
    impares = []
    # Recorremos el rango en orden inverso usando range con un paso de -1
    for num in range(fin, inicio - 1, -1):
        if num % 2 != 0:
            impares.append(str(num))
    
    # Unimos la lista de impares con comas y la imprimimos en una línea
    print(", ".join(impares))

# Ejemplo de uso:
imprimir_impares_inverso(1, 20)
