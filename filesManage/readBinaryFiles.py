# La lectura de un archivo binario requiere el uso de un método especializado llamado readinto(), ya que el método no crea un nuevo objeto del arreglo de bytes, sino que llena uno creado previamente con los valores tomados del archivo binario.
# El método devuelve el número de bytes leídos con éxito.
# El método intenta llenar todo el espacio disponible dentro de su argumento; si existen más datos en el archivo que espacio en el argumento, la operación de lectura se detendrá antes del final del archivo; el resultado del método puede indicar que el arreglo de bytes solo se ha llenado de manera fragmentaria (el resultado también lo mostrará y la parte del arreglo que no está siendo utilizada por los contenidos recién leídos permanece intacta).

# from os import strerror

# data = bytearray(10)

# try:
#     bf = open('file.bin', 'rb')
#     bf.readinto(data)
#     bf.close()

#     for b in data:
#         print(hex(b), end=' ')
# except IOError as e:
#     print("Se produjo un error de E/S: ", strerr(e.errno))

# Primero, abrimos el archivo (el que se creó usando el código anterior) con el modo descrito como rb.
# Luego, leemos su contenido en el arreglo de bytes llamado data, con un tamaño de diez bytes.
# Finalmente, imprimimos el contenido del arreglo de bytes

#---------------------------------------------------------------------------------------

# Se ofrece una forma alternativa de leer el contenido de un archivo binario mediante el método denominado read().
# Invocado sin argumentos, intenta leer todo el contenido del archivo en la memoria, haciéndolo parte de un objeto recién creado de la clase bytes.
# Esta clase tiene algunas similitudes con bytearray, con la excepción de una diferencia significativa: es immutable.

# from os import strerror

# try:
#     bf = open('file.bin', 'rb')
#     data = bytearray(bf.read())
#     bf.close()

#     for b in data:
#         print(hex(b), end=' ')

# except IOError as e:
#     print("Se produjo un error de E/S: ", strerr(e.errno))

# no utilices este tipo de lectura si no estás seguro de que el contenido del archivo se ajuste a la memoria disponible

#---------------------------------------------------------------------------------------------

# Si el método read() se invoca con un argumento, se especifica el número máximo de bytes a leer.
# El método intenta leer la cantidad deseada de bytes del archivo, y la longitud del objeto devuelto puede usarse para determinar la cantidad de bytes realmente leídos.

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S:", strerr(e.errno))


# ingresa aquí el código que lee los bytes del stream

# Nota: los primeros cinco bytes del archivo han sido leídos por el código; los siguientes cinco todavía están esperando ser procesados.