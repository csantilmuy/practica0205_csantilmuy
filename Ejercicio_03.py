# Escribir una función que calcule el área de un círculo y otra que calcule el
# volumen de un cilindro usando la primera función.
def area_circulo(radio):
    """ Calcula el área de un círculo dado su radio.
    Parámetros:
    - radio: Un número real que representa el radio del círculo.
    Salida:
    Un número real que representa el área del círculo. """
    return 3.14 * radio ** 2

def volumen_cilindro(altura):
    """ Calcula el volumen de un cilindro usando el área de su base.
    Parámetros:
    - radio: Un número real que representa el radio de la base del cilindro.
    - altura: Un número real que representa la altura del cilindro.
    Salida:
    Un número real que representa el volumen del cilindro. """
    return resultado * altura
resultado = area_circulo(int(input("Dime el radio: ")))
print(resultado)
resultado1 = volumen_cilindro(int(input("Dime la altura: ")))
print(resultado1)