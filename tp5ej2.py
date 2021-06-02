################
# Jean Favreau - @JeanFranco99
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def fib(num):
    """Funcion para encontrar la posicion en fibonacci"""
    if num < 2:
        return num
    else:
        # formula recursiva de fibonacci, donde:
        # fn = fn-1 + fn-2
        return fib(num-1) + fib(num-2)


def prueba():
    numero = int(input("Ingrese la posicion a encontrar: "))
    if numero < 2:
        print("El numero tiene que ser mayor a 2")
    else:
        evaluar = fib(numero)
        print(f"La posicion {numero} en Fibonacci es el numero:" ,evaluar)

if __name__ == "__main__":
    prueba()