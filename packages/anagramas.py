cadena1 = input("Ingresa la primera cadena: ")
cadena2 = input("Ingresa la segunda cadena: ")

# esto es lo que vamos a hacer con ambas cadenas:
# - quitar los espacios
# - cambiar todas las letras a mayúsculas
# - convertirla a una lista
# - ordenar la lista
# - unir los elementos de la lista en una cadena
# y finalmente, comparar ambas cadenas
# ¡Hagámoslo!

cadenax1 = ''.join(sorted(list(cadena1.upper().replace(' ',''))))
cadenax2 = ''.join(sorted(list(cadena2.upper().replace(' ',''))))
if len(cadenax1) > 0 and cadenax1 == cadenax2:
	print("Anagramas")
else:
	print("No son Anagramas")