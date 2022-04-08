class Super:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Mi nombre es " + self.nombre + "."

class Sub(Super):
    def __init__(self, nombre):
        Super.__init__(self, nombre)
        # super().__init__(nombre)

obj = Sub("Andy")

print(obj)


# Existe una clase llamada Super, que define su propio constructor utilizado para asignar la propiedad del objeto, llamada nombre.
# La clase también define el método __str__(), lo que permite que la clase pueda presentar su identidad en forma de texto.
# La clase se usa luego como base para crear una subclase llamadaSub. La clase Sub define su propio constructor, que invoca el de la superclase. Toma nota de cómo lo hemos hecho: Super.__init__(self, nombre).
# Tambien se puede usar super().__init__(nombre), La función super() crea un contexto en el que no tiene que (además, no debe) pasar el argumento propio al método que se invoca; es por eso que es posible activar el constructor de la superclase utilizando solo un argumento.
# puedes usar este mecanismo no solo para invocar al constructor de la superclase, pero también para obtener acceso a cualquiera de los recursos disponibles dentro de la superclase.
# Hemos nombrado explícitamente la superclase y hemos apuntado al método para invocar a __init__(), proporcionando todos los argumentos necesarios.
# Hemos instanciado un objeto de la clase Sub y lo hemos impreso.
# Como no existe el método __str__() dentro de la clase Sub, la cadena a imprimir se producirá dentro de la clase Super. Esto significa que el método __str__() ha sido heredado por la clase Sub.