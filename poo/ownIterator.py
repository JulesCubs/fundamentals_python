# def potenciasDe2(n):
#     potencia = 1
#     for i in range(n):
#         yield potencia
#         potencia *= 2

# for v in potenciasDe2(8):
#     print(v)

# Los generadores también pueden usarse dentro de listas de comprensión, como aqui:

# def potenciasDe2(n):
#     potencia = 1
#     for i in range(n):
#         yield potencia
#         potencia *= 2

# t = [x for x in potenciasDe2(5)]

# print(t)

# La función list() puede transformar una serie de invocaciones de generador subsequentes en una lista real:

# def potenciasDe2(n):
#     potencia = 1
#     for i in range(n):
#         yield potencia
#         potencia *= 2

# t = list(potenciasDe2(3))

# print(t)

# El contexto creado por el operador in también te permite usar un generador.

# El ejemplo muestra cómo hacerlo:

def potenciasDe2(n):
    potencia= 1
    for i in range(n):
        yield potencia
        potencia*= 2

for i in range(20):
    if i in potenciasDe2(4):
        print(i)