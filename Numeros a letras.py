from num2words import num2words
def numeroaletra(numero):
        numero = float(numero)
        if numero == 0:
            return "cero"
        else:
            letras = num2words(numero, lang='es')
            return letras
numero = input("Introduce un numero: ")
resultado = numeroaletra(numero)
print("El numero en letras es:", resultado)
