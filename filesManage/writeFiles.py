# El método se llama write() y espera solo un argumento: una cadena que se transferirá a un archivo abierto (no lo olvides), el modo de apertura debe reflejar la forma en que se transfieren los datos - escribir en un archivo abierto en modo de lectura no tendrá éxito).
# No se agrega carácter de nueva línea al argumento de write(), por lo que debes agregarlo tu mismo si deseas que el archivo se complete con varias líneas.

from os import strerror

try:
	fo = open('newtext.txt', 'wt') #un nuevo archivo (newtext.txt) es creado
	for i in range(10):
		s = "línea #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerr(e.errno))

# La cadena que se grabará consta de la palabra línea, seguida del número de línea. Hemos decidido escribir el contenido de la cadena carácter por carácter (esto lo hace el bucle interno for) pero no estás obligado a hacerlo de esta manera.
# Solo queríamos mostrarte que write() puede operar con caracteres individuales.

#-----------------------------------------------------------------------------------------

# Nota: puedes usar el mismo método para escribir en el stream stderr, pero no intentes abrirlo, ya que siempre está abierto implícitamente.

from os import strerror

try:
	fo = open('newtext.txt', 'wt')
	for i in range(10):
		fo.write("line #" + str(i+1) + "\n")
	fo.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerr(e.errno))