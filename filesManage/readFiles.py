# from os import strerror

# try:
#     cnt = 0
#     s = open('text.txt', "rt")
#     ch = s.read(1)
#     while ch != '':
#         print(ch, end='')
#         cnt += 1
#         ch = s.read(1)
#     s.close()
#     print("\n\nCaracteres en el archivo: ", cnt)
# except IOError as e:
#     print("Se produjo un error de E/S: ", strerr(e.errno))


# Se usa el mecanismo try-except y se abre el archivo con el nombre (text.txt en este caso).
# Intenta leer el primer caracter del archivo (ch = s.read(1)).
# Si tienes éxito (esto se demuestra por el resultado positivo de la condición while), se muestra el caracter (nota el argumento end=,¡es importante! ¡No querrás saltar a una nueva línea después de cada caracter!).
# Se actualiza el contador (cnt).
# Intenta leer el siguiente carácter y el proceso se repite.

# -------------------------------------------------------------------------------

# Si estás absolutamente seguro de que la longitud del archivo es segura y puedes leer todo el archivo en la memoria de una vez, puedes hacerlo: la función read(), invocada sin ningún argumento o con un argumento que se evalúa a None, hará el trabajo por ti.

# el leer un archivo muy grande (en terabytes) usando este método puede dañar tu sistema operativo.

# from os import strerror

# try:
#     cnt = 0
#     s = open('text.txt', "rt")
#     content = s.read()
#     for ch in content:
#         print(ch, end='')
#         cnt += 1
#         ch = s.read(1)
#     s.close()
#     print("\n\nCaracteres en el archivo: ", cnt)
# except IOError as e:
#     print("Se produjo un error de E/S: ", strerr(e.errno))


# Abre el archivo, como anteriormente se hizo.
# Lee el contenido mediante una invocación de la función read().
# Despues, se procesa el texto, iterando con un bucle for su contenido, y se actualiza el valor del contador en cada vuelta del bucle.

#------------------------------------------------------------------------

# Si deseas manejar el contenido del archivo como un conjunto de líneas, no como un montón de caracteres, el método readline() te ayudará con eso.
# El método intenta leer una línea completa de texto del archivo, y la devuelve como una cadena en caso de éxito. De lo contrario, devuelve una cadena vacía.
# Esto abre nuevas oportunidades: ahora también puedes contar líneas fácilmente, no solo caracteres.

# from os import strerror

# try:
#     ccnt = lcnt = 0
#     s = open('text.txt', 'rt')
#     line = s.readline()
#     while line != '':
#         lcnt += 1
#         for ch in line:
#             print(ch, end='')
#             ccnt += 1
#         line = s.readline()
#     s.close()
#     print("\n\nCaracteres en el archivo: ", ccnt)
#     print("Lineas en el archivo:     ", lcnt)
# except IOError as e:
#     print("Se produjo un error de E/S: ", strerr(e.errno))


# ---------------------------------------------------------------------------------------

# Otro método, que maneja el archivo de texto como un conjunto de líneas, no como caracteres, es readlines().
# Cuando el método readlines(), se invoca sin argumentos, intenta leer todo el contenido del archivo y devuelve una lista de cadenas, un elemento por línea del archivo.
# Si no estás seguro de si el tamaño del archivo es lo suficientemente pequeño y no deseas probar el sistema operativo, puedes convencer al método readlines() de leer no más de un número especificado de bytes a la vez (el valor de retorno sigue siendo el mismo, es una lista de una cadena).


# El tamaño máximo del búfer de entrada aceptado se pasa al método como argumento.
# Puedes esperar que readlines() procese el contenido del archivo de manera más efectiva que readline(), ya que puede ser invocado menos veces.
# Nota: cuando no hay nada que leer del archivo, el método devuelve una lista vacía. Úsalo para detectar el final del archivo.
# Puedes esperar que al aumentar el tamaño del búfer mejore el rendimiento de entrada, pero no hay una regla de oro para ello: intenta encontrar los valores óptimos por ti mismo.

from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCaracteres en el archivo: ", ccnt)
    print("Lineas en el archivo:     ", lcnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))

# Hemos decidido usar un búfer de 15 bytes de longitud. No pienses que es una recomendación.
# Hemos utilizado ese valor para evitar la situación en la que la primera invocación de readlines() consuma todo el archivo.
# Queremos que el método se vea obligado a trabajar más duro y que demuestre sus capacidades.
# Existen dos bucles anidados en el código: el exterior emplea el resultado de readlines() para iterar a través de él, mientras que el interno imprime las líneas carácter por carácter.

#--------------------------------------------------------------------------------------------------------

# El último ejemplo que queremos presentar muestra un rasgo muy interesante del objeto devuelto por la función open() en modo de texto.
# El objeto es una instancia de la clase iterable.
# El protocolo de iteración definido para el objeto del archivo es muy simple: su método __next__ solo devuelve la siguiente línea leída del archivo.
# Además, puedes esperar que el objeto invoque automáticamente a close() cuando cualquiera de las lecturas del archivo lleguen al final del archivo.

from os import strerror

try:
	ccnt = lcnt = 0
	for line in open('text.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCaracteres en el archivo: ", ccnt)
	print("Lineas en el archivo:     ", lcnt)
except IOError as e:
	print("Se produjo un error de E/S: ", strerr(e.errno))

#-------------------------------------------------------------------------------------------------------------------