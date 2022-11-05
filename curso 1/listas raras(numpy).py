import numpy as np

a = np.array([0,1,2,3,4,5])

print(type(a))
print(a.size)

u = np.array([8,31])
v = np.array([10,2])
z = u + v
print(z)

r = 6 * z
print(r)

n = u * v
print (n)

k = np.dot(u,v) # n1 * n2 + y1 * y2
print(k)

l = a + 4 # me suma 4 a cada elemento del vector
print(l)

promedio = a.mean() # saca el promedio de los numeros
print(promedio)

#---------------------------------------------------------------#

x = np.array([0,np.pi,np.pi/2])

y = np.sin(x) # le hago el seno a cada numero

print(y)

#---------------------------------------------------------------#

t = np.linspace(-2,2,num=5) # aca le digo que vaya de -2 a 2 con la misma graduacion entre cada numero y que en total sean 5 numeros
print(t)

p = np.linspace (0 , 2*np.pi ,num=100) # podes obviar el num = 100 y escribir solo 100
y = np.sin(x)
import matplotlib.pyplot as plt
#%matplotlib inline   #salta un error ni idea para mi falta codigo deberia hacerse un grafico
plt.plot(x,y)

print(p)

