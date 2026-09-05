a= 7
b= 2

#print(a + b)  # suma
#print(a - b)  # resta
#print(a * b)  # multiplicacion 
#print(a / b)  # division
#print(a // b) # division entera 
#print(a % b)  # modelo (el residuo de la division)
#print(a ** b) # potencia

#print(a > b, a == b, a != b)

#distancia_metros = 1500
#vuelta_metros = 400

#vueltas_completas = (distancia_metros // vuelta_metros)
#print("Puedes dar", vueltas_completas, "vueltas completas")

#metros_sobrantes = (distancia_metros % vuelta_metros)
#print("Sobran", metros_sobrantes,"metros")


#temperatura_corporal = float (input("cual es tu temperatura en grados celcius?"))
#print(f"tu temperatura en celcius es {temperatura_corporal}")

#farenheit = temperatura_corporal * 9/5 + 32
#print (f"tu temperatura en farenheit es {farenheit}") 


edades = [55, 30, 17, 28, 27]

for edad in edades:
    if edad >= 55:
        print(f"{edad} años: persona adulta")
    elif edad >= 30:
        print(f"{edad} años: persona promedio")
    else:
        print(f"{edad} años: persona joven")

