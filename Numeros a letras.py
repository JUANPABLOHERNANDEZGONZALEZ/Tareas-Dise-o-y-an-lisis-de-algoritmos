from num2words import num2words
numero = input("Introduce un numero: ")
numero = float(numero)
letras = num2words(numero, lang='es')
print("El numero en letras es:", letras)
