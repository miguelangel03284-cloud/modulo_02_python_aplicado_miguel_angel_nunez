"""
EJERCICIO PRACTICO

1. crear un diccionario llamado" producto"
2.las llaves(clave y valor) "nombre", "precio" y "stock"
3.agregar una nueva llave llamada "categoria"
4.modificar el valor de la llave "precio" sumandole 10 al valor original.
"""
"""
producto ={"nombre:""manzana","precio":200, "stock:"10}
print(producto)

producto["categoria"] = "frutas"
print(producto)

producto["precio"] = producto["precio"] + 10
print(producto)
"""
"""
inventario={"manzana":50, "peras":30, "uvas":80}

for producto,stocks in inventario.items():
    if stocks >= 40:
        print(producto, "tienes stock suficientes")
    else:
        print(producto, "no tienes stock suficientes")    
"""

"""

inventario={"manzana":50, "peras":30, "uvas":80}

if inventario.items() >= 40:
    print("tienes stock disponibles")
else:
    print("no tienes suficiente stock")    

"""


repuesta = ["python", "java","python", "c++", "python", "java"]

sin_repetir = set(repuesta)
print( sin_repetir)
print("-----------------")

elementos_en_numeros = len(sin_repetir)

print(f"total de elementos en numeros: {elementos_en_numeros}")
print(f"elementos organizados en orden alfabetico: {sorted(sin_repetir)}")







