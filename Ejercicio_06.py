# Escribir una función que convierta un número decimal en binario y otra que
# convierta un número binario en decimal.
def decimal_a_binario(decimal):
    """ Función que convierte un número decimal en binario. """
    return bin(decimal)[2:]

def binario_a_decimal(binario):
    """ Función que convierte un número binario en decimal. """
    return int(binario, 2)

decimal = int(input("Ingrese un número decimal: "))
print("El número decimal", decimal, "en binario es:", decimal_a_binario(decimal))

binario = input("Ingrese un número binario: ")
print("El número binario", binario, "en decimal es:", binario_a_decimal(binario))