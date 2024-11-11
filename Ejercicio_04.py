# Escribir una función que reciba una muestra de números en una lista y
# devuelva su media.
def calcular_media(muestra):
    """ Función que calcula la media de una lista de números.
    Parámetros:
    - muestra: Lista de números reales.
    Salida:
    Un número real que representa la media de los valores en la lista
    proporcionada. """
    return sum(muestra) / len(muestra)
entrada = input("Ingrese los números de la muestra separados por espacios: ")
muestra = list(map(float, entrada.split()))
media = calcular_media(muestra)
print("La media de la muestra es:", media)