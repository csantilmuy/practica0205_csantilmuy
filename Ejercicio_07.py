# Escribir una función que reciba un fragmento de texto en una cadena de
# caracteres y devuelva un diccionario con cada palabra que contiene y su
# frecuencia. Escribir otra función que reciba el diccionario generado con la
# función anterior y devuelva una tupla con la palabra más repetida y su
# frecuencia.
def contar_palabras(texto):
    """ Función que recibe un fragmento de texto y devuelve un diccionario
    con cada palabra y su frecuencia. """
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

def palabra_mas_repetida(diccionario):
    """ Función que recibe un diccionario de palabras y frecuencias,
    y devuelve una tupla con la palabra más repetida y su frecuencia. """
    palabra_frecuente = max(diccionario.items(), key=lambda x: x[1])
    return palabra_frecuente

texto = input("Ingrese un fragmento de texto: ")

frecuencia_palabras = contar_palabras(texto)
print("Frecuencia de palabras:", frecuencia_palabras)

mas_repetida = palabra_mas_repetida(frecuencia_palabras)
print("La palabra más repetida es:", mas_repetida[0],", " "con una frecuencia de:", mas_repetida[1])