################
# Jean Favreau - @JeanFranco99
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def fibo(num):
    """Funcion para encontrar la posicion en fibonacci"""
    if num < 2:
        return num
    else:
        # formula recursiva de fibonacci, donde:
        # fn = fn-1 + fn-2
        return fibo(num-1) + fibo(num-2)


def prueba():
    numero = int(input("Ingrese la posicion a encontrar: "))
    if numero < 2:
        print("El numero tiene que ser mayor a 2")
    else:
        evaluar = fibo(numero)
        print(f"La posicion {numero} en Fibonacci es el numero:" ,evaluar)

if __name__ == "__main__":
    prueba()