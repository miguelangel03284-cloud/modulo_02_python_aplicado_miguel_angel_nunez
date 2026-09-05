#Crea	4	variables	que	describan	un	producto	de	una	tienda:	producto	(el	nombre,	texto),	precio	(un	número	con	decimales),	en_oferta	(verdadero	o
#falso),	y	cantidad_stock	(un	número	entero).	Imprime	cada	una,	y	después	imprime	el	tipo	de	las	4	juntas	con	type().
"""
producto = "Audifonos inalambricos"
precio = 45.99
en_oferta = True
cantidad_stock = 120

print(producto)
print(precio)
print(en_oferta)
print(type(producto),type(precio),type(en_oferta),type(cantidad_stock))

"""
#Una	compra	cuesta	18.75	y	el	cliente	paga	con	un	billete	de	20.	Calcula	e	imprime	el	vuelto	exacto
"""
total_compra = 18.75
pago_cliente = 20
vuelto = pago_cliente - total_compra

print(f"vuelto: {vuelto}")
"""

#Un	cajero	tiene	que	dar	37	dólares	en	cambio,	usando	la	menor	cantidad	posible	de	billetes	de	10.	Calcula	cuántos	billetes	de	10	completos	puede	dar,	y
#cuánto	sobra	en	billetes	más	pequeños.
"""
monto = 48.48
billetes_de_diez = monto // 10
sobrante = monto % 10

print("billetes de diez:", billetes_de_diez, "sobrante:", sobrante)
"""

#Pídele	al	usuario	2	números	distintos,	uno	a	la	vez,	con	input().	Conviértelos	a	número,	y	muestra	con	un	f-string	la	suma	de	ambos.
"""
primer_numero = float(input("Escribe el primer numero: "))
segundo_numero = float(input("Escribe el segundo numero: "))

suma = primer_numero + segundo_numero
print(f"La suma de {primer_numero} y {segundo_numero} es {suma}")
"""

#Crea	una	variable	nota	con	un	número	del	0	al	100.	Clasifícala	en	una	letra:	"A"	si	es	90	o	más,	"B"	si	es	80	o	más,	"C"	si	es	70	o	más,	y	"F"	en
#cualquier	otro	caso.	Imprime	la	nota	junto	con	su	letra.
"""
nota = 100

if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
else:
    letra = "F"

print(f"Nota {nota}: {letra}")
"""

"""
Una	tienda	da	descuento	según	el	monto	total	de	la	compra:	15%	si	la	compra	es	de	$200	o	más,	10%	si	es	de	$100	a	$199,	y	sin	descuento	si	es
menos	de	$100.	Pídele	al	usuario	el	monto	de	su	compra	con	input(),	calcula	el	descuento	que	le	corresponde,	y	muestra	con	f-strings	el	monto
original,	el	porcentaje	de	descuento	aplicado,	y	el	precio	final	después	del	descuento
"""
"""
monto_compra = float(input("Ingrese el motno de la compra: "))

if monto_compra >= 200:
    descuento = 0.15
elif monto_compra >= 100:
    descuento = 0.10
else:
    descuento = 0

precio_final = monto_compra - (monto_compra * descuento)

print(f"Monto original: ${monto_compra}")
print(f"Descuento aplicado: {int(descuento*100)}%")
print(f"Precio final: ${precio_final}")
"""

"""
Pídele	al	usuario	el	monto	de	la	cuenta	de	un	restaurante	y	la	cantidad	de	personas	en	la	mesa,	ambos	con	input().	Calcula	la	propina	sugerida	según
estas	reglas:
·	Si	la	cuenta	es	menor	a	$20,	la	propina	es	del	10%.
·	Si	la	cuenta	es	de	$20	a	$50,	la	propina	es	del	15%.
·	Si	la	cuenta	es	mayor	a	$50,	la	propina	es	del	20%.
·	Si	además	son	más	de	4	personas	en	la	mesa,	agrega	un	5%	adicional	a	la	propina,	sin	importar	el	monto	de	la	cuenta.
Muestra	con	f-strings:	el	monto	de	la	propina,	el	total	a	pagar	(cuenta	más	propina),	y	cuánto	le	toca	pagar	a	cada	persona	si	se	divide	el	total	entre
todos

"""
cuenta = float(input("Ingrese monto a pagar: "))
personas = int(input("Ingrese cantidad de personas en la mesa: "))

if cuenta <= 20:
    propina = cuenta * 0.10
elif cuenta <= 50:
    propina = cuenta * 0.15
else:
    propina = cuenta * 0.20

if personas > 4:
    propina = propina + (cuenta * 0.05)

monto_propina = propina
total_a_pagar = cuenta + propina
pagar_por_persona = total_a_pagar / personas

print(f"Monto de la propina: ${monto_propina}")
print(f"Total a pagar: ${total_a_pagar}")
print(f"Total a pagar por persona: ${pagar_por_persona}")




                
