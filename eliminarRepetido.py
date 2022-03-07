Version Larga
miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# coloca tu código aquí
#
i = 0
contar = 0
nuevaLista = miLista[:]

while i < len(miLista):
    if miLista[i] in nuevaLista:
        for j in range(len(nuevaLista)):
            if miLista[i] == nuevaLista[j]:
                contar += 1
                if contar > 1:
                    nuevaLista[j] = ''
    contar = 0
    i += 1

i = 0
while i < len(nuevaLista):
    if nuevaLista[i] == '':
        del nuevaLista[i]
        i -= 1 
    i += 1
    
miLista = nuevaLista[:]
print("La lista solo con elementos únicos:")
print(miLista)



version corta
miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
nuevaLista = []
# Explorar todos los números de la lista original
for i in range(len(miLista)):
    if miLista[i] not in nuevaLista:
        nuevaLista.append(miLista[i])
    # Si el número no aparece en la nueva lista ...
        # ... agregarlo aquí.
# Hacer una copia de nuevaLista.
miLista = nuevaLista[:]
print("La lista solo con elementos únicos:")
print(miLista)