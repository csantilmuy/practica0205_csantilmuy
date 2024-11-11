# Escribir una función que reciba una muestra de números en una lista y
# devuelva otra lista con sus valores al cuadrado.
def cuadrados(muestra):
    """ Función que recibe una lista de números y devuelve otra lista con los
    valores al cuadrado. """
    return [x ** 2 for x in muestra]
muestra = list(map(float, input("Ingrese los números de la muestra separados por espacios: ").split()))
print("Los valores al cuadrado de la muestra son:", cuadrados(muestra))