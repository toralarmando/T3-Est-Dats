#OBTENER FIBONACCI EN MODO ITERATIVO EN Python
def fibonacci_iterativo(posicion, debe_imprimir):
    actual = 0
    siguiente = 1
    for x in range(posicion + 1):
        if debe_imprimir:
            print(str(actual) + ",", end=" ")
        temporal = actual
        actual = siguiente
        siguiente = siguiente + temporal
    return temporal
    
posicion = 10

print(f"Imprimiendo serie hasta posición {posicion}")

fibonacci_iterativo(posicion, True)
valor = fibonacci_iterativo(posicion, False)

print(f"\nFibonacci de {posicion} con método iterativo es {valor}")

#Para cambiar el valor de la serie fibonacci se debe cambiar la variable posicion de la linea 12