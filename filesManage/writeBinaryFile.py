# Primero, inicializamos bytearray con valores a partir de 10; si deseas que el contenido del archivo sea claramente legible, reemplaza el 10 con algo como ord('a'), esto producirá bytes que contienen valores correspondientes a la parte alfabética del código ASCII (no pienses que harás que el archivo sea un archivo de texto; sigue siendo binario, ya que se creó con un indicador - bandera wb).
# Después, creamos el archivo usando la función open(), la única diferencia en comparación con las variantes anteriores es que el modo de apertura contiene el indicador b.
# El método write() toma su argumento (bytearray) y lo envía (como un todo) al archivo.
# El stream se cierra de forma rutinaria.
# El método write() devuelve la cantidad de bytes escritos correctamente.
# Si los valores difieren de la longitud de los argumentos del método, puede significar que hay algunos errores de escritura.
# En este caso, no hemos utilizado el resultado; esto puede no ser apropiado en todos los casos.

# from os import strerror

# data = bytearray(10)

# for i in range(len(data)):
#     data[i] = 10 + i

# try:
#     bf = open('file.bin', 'wb')
#     bf.write(data)
#     bf.close()
# except IOError as e:
#     print("Se produjo un error de E/S: ", strerr(e.errno))

