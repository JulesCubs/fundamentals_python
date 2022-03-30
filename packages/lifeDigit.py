fecha = input("Ingresa tu fecha de cumpleaños (en el siguiente formato: AAAAMMDD o AAAADDMM, 8 dígitos): ")
if len(fecha) != 8 or not fecha.isdigit():
	print("Fecha inválida - lo siento, no podemos hacer nada al respecto.")
else:
	# mientras haya más de un dígito en la fecha
	while len(fecha) > 1:
		sum = 0
		# ... sumar de todos los dígitos...
		for dig in fecha:
			sum += int(dig)
		print(fecha)
		# ... y almacenar la suma dentro de la cadena
		fecha = str(sum)
	print("Tu Dígito de la Vida es: " + fecha)