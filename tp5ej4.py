################
# Jean Favreau - @JeanFranco99
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def NumeroPerfecto(num):
    """Funcion para determinar si el numero ingresado es perfecto o no"""
    suma = 0
    for i in range(1,num):
        if (num % i == 0):
            suma = suma + i
    if num == suma:
        return True
    else:
        return False

def prueba():
    num = int(input("Introduzca un numero: "))
    if NumeroPerfecto(num):
        print(f"{num} es un numero perfecto")
    else:
        print(f"{num} no es un numero perfecto")
        
if __name__ == "__main__":
    prueba()  