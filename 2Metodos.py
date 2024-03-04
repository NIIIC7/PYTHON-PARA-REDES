#Funcion sin parametros

def sumaPar ():
    ax=45
    bx=1
    sumax=ax+bx
sumaPar()

#funcion sin paremtros RETURN

def sumaRtn():
    yx = 4
    xy = 425
    
    suma = yx + xy
    return suma  # Returning the computed sum, not the function itself

print('Función sin parámetros con RETURN')
print(sumaRtn())  # Correctly calling the function and printing its return value


#Funcion con parametros
def suma (a,b):
    suma =a+b
    print(suma)
suma(5,8)