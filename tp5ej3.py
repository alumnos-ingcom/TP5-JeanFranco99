################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def trib(num):
    """Funcion para encontrar la posicion en tribonacci"""
    if num < 3:
        return num
    else:
        # formula recursiva de tribonacci, donde:
        # fn = fn-1 + fn-2 + fn-3
        return trib(num-1) + trib(num-2) + trib(num-3)


def prueba():
    numero = int(input("Ingrese la posicion a encontrar: "))
    if numero < 3:
        print("El numero a ingresar tiene que ser mayor a 3")
    else:
        evaluar = trib(numero)
        print(f"La posicion {numero} en la sucesion de Tribonacci es: " ,evaluar)

if __name__ == "__main__":
    prueba()
