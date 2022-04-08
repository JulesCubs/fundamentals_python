class MiClase:
    pass

obj = MiClase()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.entero = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

# Así es como funciona:

# La línea 1: define una clase simple...
# Líneas 3 a la 10: ... la llenan con algunos atributos.
# Línea 12: ¡esta es nuestra función!
# Línea 13: escanea el atributo __dict__, buscando todos los nombres de atributos.
# Línea 14: si un nombre comienza con i...
# Línea 15: ... utiliza la función getattr() para obtener su valor actual; nota: getattr() toma dos argumentos: un objeto y su nombre de propiedad (como una cadena) y devuelve el valor del atributo actual.
# Línea 16: comprueba si el valor es de tipo entero, emplea la función isinstance().
# Línea 17: si la comprobación sale bien, incrementa el valor de la propiedad haciendo uso de la función setattr(); la función toma tres argumentos: un objeto, el nombre de la propiedad (como una cadena) y el nuevo valor de la propiedad.



