class PizzaError(Exception):
    def __init__(self, pizza, mensaje):
        Exception.__init__(self, mensaje)
        self.pizza = pizza


class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza, queso, mensaje):
        PizzaError.__init__(self, pizza, mensaje)
        self.queso = queso


def makePizza(pizza, queso):
	if pizza not in ['margherita', 'capricciosa', 'calzone']:
		raise PizzaError(pizza, "no hay tal pizza en el menú")
	if queso > 100:
		raise DemasiadoQuesoError(pizza, queso, "demasiado queso")
	print("¡Pizza lista!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
	try:
		makePizza(pz, ch)
	except DemasiadoQuesoError as tmce:
		print(tmce, ':', tmce.queso)
	except PizzaError as pe:
		print(pe, ':', pe.pizza)

# Combinamos las dos excepciones previamente definidas y las aprovechamos para que funcionen en un pequeño ejemplo.

# Una de ellas es lanzada dentro de la función hacerPizza() cuando ocurra cualquiera de estas dos situaciones erróneas: una solicitud de pizza incorrecta o una solicitud de una pizza con demasiado queso.

# Nota:

# El remover la rama que comienza con except DemasiadoQuesoError hará que todas las excepciones que aparecen se clasifiquen como PizzaError.
# El remover la rama que comienza con except PizzaError provocará que la excepción DemasiadoQuesoError no pueda ser manejada, y hará que el programa finalice.

# La solución anterior, aunque elegante y eficiente, tiene una debilidad importante. Debido a la manera algo fácil de declarar los constructores, las nuevas excepciones no se pueden usar tal cual, sin una lista completa de los argumentos requeridos.

# Eliminaremos esta debilidad estableciendo valores predeterminados para todos los parámetros del constructor. Observa:

# class PizzaError(Exception):
#     def __init__(self, pizza='desconocida', mensaje=''):
#         Exception.__init__(self, mensaje)
#         self.pizza = pizza


# class DemasiadoQuesoError(PizzaError):
#     def __init__(self, pizza='desconocida', queso='>100', mensaje=''):
#         PizzaError.__init__(self, pizza, mensaje)
#         self.queso = queso


# def hacerPizza(pizza, queso):
# 	if pizza not in ['margherita', 'capricciosa', 'calzone']:
# 		raise PizzaError
# 	if queso > 100:
# 		raise DemasiadoQuesoError
# 	print("¡Pizza lista!")


# for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
# 	try:
# 		hacerPizza(pz, ch)
# 	except DemasiadoQuesoError as tmce:
# 		print(tmce, ':', tmce.queso)
# 	except PizzaError as pe:
# 		print(pe, ':', pe.pizza)