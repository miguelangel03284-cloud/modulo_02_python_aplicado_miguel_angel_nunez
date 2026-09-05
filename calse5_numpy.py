import numpy as np

#numeros = np.array ([1,5,4,6,4,6,4])
#print(numeros)

precios = np.array([25.99, 40.50, 15.75, 60.00, 33.20])

precios_con_descuento = precios * 0.85

print(precios_con_descuento.round(2))

#indexing, slicing, funciones estadisticas

temperaturas = np.array([25.9, 40.5, 15.7, 60.2, 33.2, 27.6, 24.3 ])

#print(temperaturas[0])
#print(temperaturas[-1])
#print(temperaturas[2:5])
"""
print("promedio: ", round(np.mean(temperaturas), 2))

print("maximo: ",np.max(temperaturas))
print("minimo: ",np.min(temperaturas))
print("sumar: ",np.sum(temperaturas))
print("desviacion estandar: ",round(np.std(temperaturas), 2))
"""

"""
EJERCICIO GUIADO

1.crear su propio array, llamarlo "temperaturas_semana"
2.introducir 7 valores a su array.
3.imprimir el promedio, la maxima, la minima y la desviacion estandar
4.redondear todo los resultados a 1 decimal
"""
temperaturas_semana = np.array([20.40, 35.20, 39.60, 40.10, 37.62, 42.30, 15.52])

print("promedio: ", round(np.mean(temperaturas_semana), 1))
print("la maxima: ", round(np.max(temperaturas_semana), 1))
print("la minima: ", round(np.min(temperaturas_semana), 1))
print("desviacion estandar: ", round(np.std(temperaturas_semana), 1))

# arrays de 2 dimensiones

matriz = np.array([
   [90, 85, 78],
   [70, 88, 92],
])

print(matriz)
print(matriz.shape)
print(matriz[0][1])
