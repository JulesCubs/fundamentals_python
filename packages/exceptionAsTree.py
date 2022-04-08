def printExcTree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        printExcTree(subclass, nest + 1)

printExcTree(BaseException)

# La recursión parece ser la mejor manera de recorrerlo. La función printExcTree() toma dos argumentos:

# Un punto dentro del árbol desde el cual comenzamos a recorrerlo.
# Un nivel de anidación (lo usaremos para construir un dibujo simplificado de las ramas del árbol).
# Comencemos desde la raíz del árbol: la raíz de las clases de excepciónes de Python es la clase BaseException (es una superclase de todas las demás excepciones).

# Para cada una de las clases encontradas, se realiza el mismo conjunto de operaciones:

# Imprimir su nombre, tomado de la propiedad __name__.
# Iterar a través de la lista de subclases provistas por el método __subclasses__(), e invocar recursivamente la función printExcTree(), incrementando el nivel de anidación respectivamente.