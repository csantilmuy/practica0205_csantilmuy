# Escribir una función a la que se le pase una cadena <nombre> y muestre por
# pantalla el saludo ¡hola <nombre>!.
def saludar(nombre):
    """ Función que muestra un saludo personalizado.
    Parámetros:
    -nombre: Una cadena de texto con el nombre de la persona a saludar.
    Salida: Un mensaje en pantalla con el saludo "¡Hola <nombre>!". """
    print("¡Hola " + nombre + "!")
frase = saludar(input("Dime tu nombre: "))
print(frase)