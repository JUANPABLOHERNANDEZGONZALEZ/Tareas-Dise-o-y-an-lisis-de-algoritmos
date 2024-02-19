from num2words import num2words
numero = input("Introduce un numero: ")
numero = float(numero)
if(numero > 0 and numero <= 1000000000000000000):
    letras = num2words(numero, lang='es')
    print("El numero en letras es:", letras)
else:
    print("Numero no valido")
