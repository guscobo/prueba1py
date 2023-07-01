#def lista()



#input(int("Ingrese una nota"))
# Primera forma de convocar a una libreria
# import milibreria

# Segunda forma de convocar a una libreria
#from milibreria import *
#bienvenida()
print ("\033[H\033[J")
#import milibreria as mil

#mil.bienvenida()
#print(mil.areacirculo(10))
#print(mil.areacuadrado(2,3))

#from math import *
import math as m
'''print(pi)
print(tau)
print(e)
print (ceil(1.6))
print (floor(1.6))
print (abs(-5))
print (factorial(6))
#maximo comun multiplo
print (gcd(27,90))
print (lcm(27,90))
#trunca en el punto
print (trunc(9.23365))
print (sin(5))
print (degrees(pi))
print (radians(180))
print (sqrt(144))
print(m.isinf(67))
print(m.isfinite(67))'''

'''import random as rnd

print(rnd.random()) #aleatorio >0 o <1

a = rnd.random()

print(a*10)
print(rnd.uniform(3,7)) #aleatorio >3 o <7

print(rnd.randrange(3,7)) #aleatorio >3 o <7
print(rnd.randrange(0,100,2)) #aleatorio >1 a 100 pares
print(rnd.randrange(0,100,5)) #aleatorio >1 a 100 5 en 5
print(rnd.sample([1,4,5,6,12],2)) #aleatorio >1 a 100 pares
#print(rnd.choice([1,4,5,6,12],2)) #aleatorio >1 a 100 pares
# cantidad de milisegundos transcurridos desde el 1 de enero 1970 a la fecha
rnd.seed(25)
print(rnd.random())
#con la semilla siempre da el mismo numero aleatorios'''

#import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as npy
#lista = [1,3,5,6,7,78,56,90,34]
#lista = ([1,3,5,6,7],[78,56,90,34,56])
#plt.plot(lista)
#plt.scatter([1,3,5,6,7],[78,56,90,34,56])
'''plt.plot([1,3,5,6,7], 'go-.')
plt.plot([78,56,90,34,56], 'r^--')
plt.title("Mi Grafico en Pyton")
plt.ylabel("Eje Y")
plt.xlabel("Eje X")
plt.savefig("mi grafico en py.jpg")
plt.show()'''

#print(npy.linspace(0,2,14))
print(npy.linspace(0,1,50))

z = npy.linspace(-10,10,10)
#y = npy.sin(x)
y = (z**2)+2
plt.plot(z,y)
plt.bar(z,y)
plt.show()
# En el eje x valores numericos ojo


