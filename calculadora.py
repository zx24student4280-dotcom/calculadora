def sumar(*args):
    """Suma una cantidad variable de números."""
    return sum(args)



def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

print("Suma de 2 y 3:", sumar(2, 3))
print("Suma de 1, 2, 3, 4:", sumar(1, 2, 3, 4))
print("Resta:", restar(5, 2))
print("Multiplicación:", multiplicar(3, 4))
print("Dividir:", dividir(10, 2))
