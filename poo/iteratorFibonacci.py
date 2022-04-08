# class Fib:
# 	def init(self, nn):
# 		print("init")
# 		self.__n = nn
# 		self.__i = 0
# 		self.__p1 = self.__p2 = 1
	
# 	def __iter__(self):
# 		print("__iter__")
# 		return self
	
# 	def __next__(self):
# 		print("__next__")
# 		self.__i += 1
# 		if self.__i > self.__n:
# 			raise StopIteration
# 		if self.__i in [1, 2]:
# 			return 1
# 		ret = self.__p1 + self.__p2
# 		self.__p1, self.__p2 = self.__p2, ret
# 		return ret

# for i in Fib(10):
# 	print(i)

# Hemos creado una clase capaz de iterar a través de los primeros `n` valores (donde `n` es un parámetro del constructor) de los números de Fibonacci. Fibonacci(*Fibi*) se definen de la siguiente manera:

# $*Fib_1$ = 1* 

# $*Fib_2$ = 1* 

# $*Fib_i$ = $Fib_i$-1 + $Fib_i$-2*

# En otras palabras:

# - Los primeros dos números de la serie Fibonacci son 1.
# - Cualquier otro número de Fibonacci es la suma de los dos anteriores (por ejemplo, $Fib_3$ = 2, $Fib_4$ = 3, $Fib_5$ = 5, y así sucesivamente).

# Vamos a ver el código:

# - Líneas 2 a 6: el constructor de la clase imprime un mensaje (lo usaremos para rastrear el comportamiento de la clase), se preparan algunas variables: (`__n` para almacenar el límite de la serie, `__i` para rastrear el número actual de la serie Fibonacci, y `__p1` junto con `__p2` para guardar los dos números anteriores).
# - Líneas 8 a 10: el método `__iter__` está obligado a devolver el objeto iterador en sí mismo; su propósito puede ser un poco ambiguo aquí, pero no hay misterio; trata de imaginar un objeto que no sea un iterador (por ejemplo, es una colección de algunas entidades), pero uno de sus componentes es un iterador capaz de escanear la colección; el método `__iter__` debe **extraer el iterador y confiarle la ejecución del protocolo de iteración**; como puedes ver, el método comienza su acción imprimiendo un mensaje.
# - Líneas 12 a 21: el método `__next__` es responsable de crear la secuencia; es algo largo, pero esto debería hacerlo más legible; primero, imprime un mensaje, luego actualiza el número de valores deseados y, si llega al final de la secuencia, el método interrumpe la iteración al generar la excepción StopIteration; el resto del código es simple y refleja con precisión la definición que te mostramos anteriormente.
# - Las líneas 23 y 24 hacen uso del iterador.

# - El objeto iterador se instancia primero.
# - Después, Python invoca el método `__iter__` para acceder al iterador real.
# - El método `__next__` se invoca once veces: las primeras diez veces produce valores útiles, mientras que la ultima finaliza la iteración.

class Fib:
	def __init__(self, nn):
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1

	def __iter__(self):
		print("Fib iter")
		return self

	def __next__(self):
		self.__i += 1
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret

class Class:
	def __init__(self, n):
		self.__iter = Fib(n)

	def __iter__(self):
		print("Class iter")
		return self.__iter;

object = Class(8)

for i in object:
	print(i)

# El ejemplo muestra una solución donde el objeto iterador es parte de una clase más compleja.

# El código no es sofisticado, pero presenta el concepto de una manera clara.

# Echa un vistazo al código en el editor.

# Hemos puesto el iterador Fib dentro de otra clase (podemos decir que lo hemos compuesto dentro de la clase Class). Se instancia junto con el objeto de Class.

# El objeto de la clase se puede usar como un iterador cuando (y solo cuando) responde positivamente a la invocación __iter__ - esta clase puede hacerlo, y si se invoca de esta manera, proporciona un objeto capaz de obedecer el protocolo de iteración.

# Es por eso que la salida del código es la misma que anteriormente, aunque el objeto de la clase Fib no se usa explícitamente dentro del contexto del bucle for.

