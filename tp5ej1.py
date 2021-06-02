################
# Jean Favreau - @JeanFranco99
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def es_par_o_impar(numero):
    """Funcion para evaluar si un numero es par o impar"""
    while numero > 0:
        numero = numero - 2
    if numero == 0:
        return True
    else:
        return False

def prueba():
    num = int(input("Ingrese el numero a evaluar: "))
    evaluar = es_par_o_impar(num)
    print("El numero es par? ",evaluar)
    
if __name__ == "__main__":
    prueba()