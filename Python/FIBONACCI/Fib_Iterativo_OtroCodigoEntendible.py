#OBTENER FIBONACCI EN MODO ITERATIVO EN Python, OTRO CODIGO QUE ENCONTRE Y FUE EL QUE ME EXPLICO EN CLASE :)
def fibonacci(post=1,actual=0,iteration=9):
  i = 0
  while i <= iteration:
    nextNumber = post +actual
    
    post = actual 
    actual = nextNumber
    
    print(nextNumber)
    i +=1 
    
fibonacci()
# O tambien puede realizarse una nueva busqueda de un numero fibonachi quitando el valor de las variables establicidas en la linea 1
# Ejemplo: fibonacci(1,0,9)