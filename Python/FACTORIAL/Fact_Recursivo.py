#OBTENER FACTORIAL EN MODO RECURSIVO EN Python
def factorial_recursivo(n=10):
    if n==0 or n==1:
        resultado = 1
    elif n>1:
        resultado = n * factorial_recursivo (n-1)
    print(f"\nfactorial de {n} con método recursivo es {resultado}")
    return resultado
    
factorial_recursivo()
# O tambien puede realizarse una nueva busqueda de un numero factorial quitando el valor de las variables establicidas en la linea 1
# Ejemplo: factorial_recursivo(8)
