#OBTENER FACTORIAL EN MODO ITERATIVO EN Python
n = 10
factorial_iterativo = 1 
for i in range(1,n+1):
    factorial_iterativo = factorial_iterativo * i
    print(f"\nfactorial de {i} con método iterativo es {factorial_iterativo}")

#Para buscar otro numero factorial, hay que cambiar la variable de la linea 2