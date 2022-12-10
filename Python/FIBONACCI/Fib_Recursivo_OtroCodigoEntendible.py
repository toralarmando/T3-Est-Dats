#OBTENER FIBONACCI EN MODO RECURSIVO EN Python, OTRO CODIGO QUE ENCONTRE MAS COMPLETO
#ESTE CODIGO SI TE MUESTRA LOS NUMEROS DE LA SERIE, EN FORMA DE UN CICLO FOR EL CUAL LE TENDRAS QUE ESTABLECES LOS VALORES DE LA SERIE FIBONACCI
#EN ESTE CASO LA SERIE ESTA PUESTA DE FORMA QUE TE ARROJE HASTA EL NUMERO 10 (SIN CONTAR EL 0 Y POR ESO SE PONE DE 1 AL 11)
#SE CAMBIAN LOS VALORES EN LA LINEA NUMERO 26
# memoria: almacenara los valores previos
fibonacci_cache={}

def fibonacci(n):
    # si el valor esta almacenado en fibonacci_cache solo lo retornamos
    if(n in fibonacci_cache):
        return fibonacci_cache[n]

    if n==1:
        val=1
    elif n == 2:
        val=1
    elif n > 2:
        val = fibonacci(n-1) + fibonacci(n-2)

    # agregamos resultados a memoria fibonacci_cache
    fibonacci_cache[n] = val
    # retornamos valor
    return val


for x in range(1,11):
    print(x, " : " ,fibonacci(x))