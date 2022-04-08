from os import strerror

srcname = input("¿Nombre del archivo fuente?: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)	
dstname = input("¿Nombre del archivo de destino?: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("No se puede crear el archivo de destino: ", strerr(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("No se puede crear el archivo de destino: ", strerr(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) escritos con éxito')
src.close()
dst.close()


# Las líneas 3 a la 8: solicitan al usuario el nombre del archivo a copiar e intentan abrirlo para leerlo; se termina la ejecución del programa si falla la apertura; nota: emplea la función exit() para detener la ejecución del programa y pasar el código de finalización al sistema operativo; cualquier código de finalización que no sea 0 significa que el programa ha encontrado algunos problemas; se debe utilizar el valor errno para especificar la naturaleza del problema.
# Las líneas 9 a la 15: repiten casi la misma acción, pero esta vez para el archivo de salida.
# La línea 17: prepara una parte de memoria para transferir datos del archivo fuente al destino; Tal área de transferencia a menudo se llama un búfer, de ahí el nombre de la variable; el tamaño del búfer es arbitrario; en este caso, decidimos usar 64 kilobytes; técnicamente, un búfer más grande es más rápido al copiar elementos, ya que un búfer más grande significa menos operaciones de E/S; en realidad, siempre hay un límite, cuyo cruce no genera más ventajas; pruébalo tú mismo si quieres.
# Línea 18: cuenta los bytes copiados: este es el contador y su valor inicial.
# Línea 20: intenta llenar el búfer por primera vez.
# Línea 21: mientras se obtenga un número de bytes distinto de cero, repite las mismas acciones.
# Línea 22: escribe el contenido del búfer en el archivo de salida (nota: hemos usado un segmento para limitar la cantidad de bytes que se escriben, ya que write() siempre prefiero escribir todo el búfer).
# Línea 23: actualiza el contador.
# Línea 24: lee el siguiente fragmento de archivo.
# Las líneas 29 a la 31: limpieza final: el trabajo está hecho.