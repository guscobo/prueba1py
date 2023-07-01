print ("\033[H\033[J")

'''def areac(r):
    area = 3.14*r**2
    print(area)

areac(10)

def areac(r):
    area = 3.14*r**2
    return area

 x = areac(10)
print (x/2)'''
'''def bienvenida():
    print("Hola bienvenido al curso")
    print("Hola hoy esta nublado")
    return

# Programa principal

bienvenida()'''

'''def iva():
    impuesto = 21
    costo = int(input("Ingrese el valor del producto"))
    calculo = costo*impuesto/100
    print("El precio final es", calculo+costo) 
    return

iva()
print(type(iva))'''


'''def bienvenida(nombre,apellido):
    print("Hola")
    print(nombre, apellido)
    print("bienvenido al curso")
    return

# Programa principal
bienvenida("Juan", "Perez")'''

'''def bienvenida(nombre,apellido):
    print("Hola")
    print(nombre, apellido)
    print("bienvenido al curso")
    return

# Programa principal
bienvenida(apellido = "Perez",nombre = "Juan")'''

'''def suma(a,b):
   x = a + b
    
    return x

# Programa principal
print(suma(10,5))'''


'''def operaciones(a,b):
 
    
    return a+b, a*b, a-b, a/b

# Programa principal
print(list(operaciones(10,5)))'''

'''def bienvenida(nombre,apellido="..."):
    # los valores por defecto van a lo ultimo de la funcion (utimo argumento)
    print("Hola")
    print(nombre, apellido)
    print("bienvenido al curso")
    return

# Programa principal
bienvenida(apellido = "Cobo",nombre = "Juan")'''

'''def menu(*platos):
    print("el menu del dia es: ")
    #  print("el menu del dia es: ", end="")
    for i in platos:
        print(i, end=", ")
    return

# Programa principal
menu("Fideos con tuco","Mila","Ravioles")'''

'''def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    return

print(factorial(30))'''


'''def factorial2(n):
    a = 1
    for i in range(1,n+1):
        a = a * i
    return a
    

print(factorial2(5))'''

'''def bienvenida(nombre):
    apellido = "Perez"
    print("Bienvenido", nombre, apellido)
    return

print (bienvenida("Juan"))'''

def norecomendado(a):
    global as int(a)
    a = 30
    print("El valor de la variable a en la funciones", a)
    return

#progama principal
a = 5
norecomendado()
print("El valor de la variable a en el programa principal es: ", a)






