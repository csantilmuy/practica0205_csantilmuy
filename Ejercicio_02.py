# Escribir una función que reciba un número entero positivo y devuelva su
# factorial. Realiza el ejercicio mediante bucles interactivos y mediante una
# función recursiva.
def factorial_iterativo(n):
    """ Calcula el factorial de un número entero positivo usando un bucle
    iterativo.
    Parámetros:
    - n: Un número entero positivo cuyo factorial se desea calcular.
    Salida:
    Un número entero que representa el factorial de n. """
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    """ Calcula el factorial de un número entero positivo de forma recursiva.
    Parámetros:
    - n: Un número entero positivo cuyo factorial se desea calcular.
    Salida:
    Un número entero que representa el factorial de n. """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)
resultado = factorial_iterativo(int(input("Dime un número: ")))
print(resultado)