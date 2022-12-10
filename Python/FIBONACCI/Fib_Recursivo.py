#OBTENER FIBONACCI EN MODO RECURSIVO EN Python
def fibonacci_recursivo(posicion):
    actual = 0
    siguiente = 1
    if posicion < 2:
        return posicion
    return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)
    
posicion = 10

valor = fibonacci_recursivo(posicion)

print(f"Fibonacci de {posicion} con método recursivo es {valor}")