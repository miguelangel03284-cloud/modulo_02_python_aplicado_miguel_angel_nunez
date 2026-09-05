import numpy as np
"""
INSTRUCCIÓN
Crea	un	array	calificaciones	con	6	notas	de	examen	(invéntalas).	Imprime	la	primera	nota,	la	última,	y	las	notas	de	la	posición	2	a	la	5	(sin	incluir	la	5).	Imprime
también	cuántas	notas	hay	en	total.
"""

# calificaciones = np.array([75, 86, 94, 72, 80, 98])

# print(calificaciones[0])
# print(calificaciones[-1])
# print(calificaciones[2:5])
# print(calificaciones)

"""
INSTRUCCIÓN
Crea	un	array	comisiones	con	4	montos	de	comisión	de	ventas	(invéntalos).	Aplica	un	bono	del	10%	a	todas	a	la	vez	(multiplica	por	1.10),	sin	usar	ningún	bucle,	y
redondea	el	resultado	a	2	decimales.
"""

# comisiones = np.array([234, 635, 48, 245])

# comisiones_bonos = comisiones * 1.10

# print(comisiones_bonos.round(2))

"""
INSTRUCCIÓN
Crea	un	array	consumo_gb	con	el	consumo	de	datos	móviles	(en	GB)	de	7	días	distintos	(invéntalos).	Imprime	el	promedio,	el	máximo,	el	mínimo,	y	la	desviación
estándar,	redondeados	a	2	decimales
"""

# consumo_gb = np.array([10.5, 3.2, 21.6, 34.1, 30.9, 9.2, 7.3, 4.9, 8.15])

# print(f"consumo promedio: ",round(np.mean(consumo_gb), 2))
# print(f"maximo: ", np.max(consumo_gb))
# print(f"maximo: ", np.min(consumo_gb))
# print(f"desviacion estandar: ", round(np.std(consumo_gb), 2))

"""
Arrays	de	2	dimensiones
Recordatorio:	
axis=1	calcula	por	fila,	
axis=0	calcula	por	columna.

INSTRUCCIÓN
Con	esta	matriz,	donde	cada	fila	es	un	estudiante	y	cada	columna	es	una	semana	de	horas	de	estudio,	calcula	el	promedio	de	horas	de	cada	estudiante,	y	el	promedio	de
cada	semana	entre	todos	los	estudiantes.
"""

# horas_estudio =	np.array([
# [5,	8,	6,	7],
# [10, 9,	11,	8],
# [3,	4,	2,	5],
# ])

# print(horas_estudio.shape)
# # print(f"Promedio por estudiante: ", np.mean(horas_estudio, axis=1))
# # print(f"Promedip por semana: ", np.mean(horas_estudio, axis=0))

"""
INSTRUCCIÓN
Con	esta	matriz	de	ventas	(3	sucursales,	5	días	de	la	semana):
Calcula:	(1)	el	total	de	ventas	de	cada	sucursal	en	la	semana,	(2)	una	comisión	del	5%	sobre	el	total	de	cada	sucursal,	y	(3)	el	total	de	ventas	combinadas	de	las	3
sucursales,	por	cada	día	de	la	semana.
"""

# ventas	=	np.array([
# [1563,	1365,	795,	1697,	1035],
# [230,	654,	1123,	369,	426],
# [1542,	1732,	1341,	1963,	1250],
# ])

# print(f"Total de ventas sucursal: ", np.sum(ventas, axis=1))
# print(f"comision 5% sucursal: ", np.sum(ventas, axis=1) * 0.05)
# print(f"total ventas de sucursales por dia: ", np.sum(ventas, axis=0))

"""
INSTRUCCIÓN
Usando	la	misma	matriz	ventas	del	Desafío	Final:	determina	cuál	de	las	3	sucursales	tiene	las	ventas	más	consistentes	a	lo	largo	de	la	semana	(la	que	menos	varía	día
a	día,	no	la	que	más	vende).	Imprime	el	resultado	de	las	3	sucursales	para	poder	comparar.
"""

ventas	=	np.array([
[1563,	1365,	795,	1697,	1035],
[230,	654,	1123,	369,	426],
[1542,	1732,	1341,	1963,	1250],
])

print(f"Desviacion estandar sucursal 1: ", round(np.std(ventas[0]), 2))
print(f"Desviacion estandar sucursal 2: ", round(np.std(ventas[1]), 2))
print(f"Desviacion estandar sucursal 3: ", round(np.std(ventas[2]), 2))