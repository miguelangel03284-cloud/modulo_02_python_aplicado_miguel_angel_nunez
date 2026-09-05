"""
edades = [24, 31, 19, 45, 27]

suma = 0
for edad in edades:
    suma += edad

print("suma total", suma)
print("promedio", suma / len(edades))

"""

"""
con la misma lista que utilizamos "edades" contar cuantas edades son mayores o iguales a 30, utilizar el bucle "for" y una variable contadora

"""
"""
edades = [24, 31, 19, 45, 27]
contador = 0
for edad in edades:
   if edad >= 30:
        contador += 1       
print(contador)

"""    
"""
contador = 5
while contador >= 0:
    print("conteo regresivo", contador)
    contador -= 1
print("despegamos !!!")    

"""
#funciones

def calcular_imc (peso, altura):
    imc = peso / (altura ** 2)
    return imc

resultado = calcular_imc (150, 1.85 )
print(f"IMC: , {round(resultado), 2}" )
