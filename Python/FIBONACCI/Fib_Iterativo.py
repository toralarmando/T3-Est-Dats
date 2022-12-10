#OBTENER FIBONACCI EN MODO ITERATIVO EN Python
def fibonacci(post=1,actual=0,iteration=9):
  i = 0
  while i <= iteration:
    nextNumber = post +actual
    
    post = actual 
    actual = nextNumber
    
    print(nextNumber)
    i +=1 
    
fibonacci()
# O tambien puede realizarse una nueva busqueda de un numero fibonachi quitando el valor de las variables establEcidas en la linea 1
