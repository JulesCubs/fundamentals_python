bloques = int(input("Ingrese el número de bloques:"))

#
# Escribe tu código aquí.
#
bloque = 1
altura = 0

while bloque <= bloques:
    valor = (8*bloque + 1)**0.5
    if valor - int(valor) == 0:
        altura += 1
    bloque += 1
print("La altura de la pirámide:", altura)