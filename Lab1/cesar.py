import sys

def cifrar_cesar(texto, corrimiento):
    texto_cifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            if caracter.islower():
                nuevo_caracter = chr(((ord(caracter) - ord('a') + corrimiento) % 26) + ord('a'))
            else:
                nuevo_caracter = chr(((ord(caracter) - ord('A') + corrimiento) % 26) + ord('A'))
            texto_cifrado += nuevo_caracter
        else:
            texto_cifrado += caracter
    return texto_cifrado

if len(sys.argv) != 3:
    print("Uso: python cifrado_cesar.py <texto> <corrimiento>")
    sys.exit(1)

texto = sys.argv[1]
corrimiento = int(sys.argv[2])

texto_cifrado = cifrar_cesar(texto, corrimiento)
print(texto_cifrado)

