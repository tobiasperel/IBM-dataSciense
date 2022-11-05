import numpy as np

a = [[0,1,2],[4,1,5],[9,8,2],[1,1,5]]

b = np.array(a)

print(b.ndim) # las dimensiones. Una dimension es un array. Al tener otro adentro tenes dos dimensiones y asi.

print(b.shape) # la cantidad de arrays por la cantidad de cada uno

print(b.size) # cantidad de elementos

c = [[1,4,6],[9,4,2],[1,3,3],[4,3,8]]
d = np.array(c)
e = a + d # suman c[0][0] con a [0][0] y asi sucesivamente
print(e,)

print("")
print("----------------------")
print("")

l = e * 4 # puedo cuadruplicar el array
print(l)

g = a * d # puedo multiplicarlos y asi