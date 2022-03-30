# Cifrado cesar con numero de cambio para cifrar
# Ingresa el texto a encriptar
texto= input("Ingresa un mensaje: ")

# Ingresa un valor de cambio válido (repitelo hasta que tengas éxito)
shift = 0

while shift == 0:
    try:    
        shift = int(input("Ingresa el valor de cambio del cifrado (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Valor de cambio inválido!")

cifrado = ''

for char in texto:
    # ¿Es un letra?
    if char.isalpha():
        # cambia su código
        code = ord(char) + shift
        # encuentra el código de la primera letra (mayúscula o minúscula)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # hacer corrección
        code -= first
        code %= 26
        # agrega caracter codificado al mensaje
        cifrado += chr(first + code)
    else:
        # agregar caracter original al mensaje
        cifrado += char

print(cifrado)