################
# Jean Favreau - @JeanFranco99
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def inversion(texto):
    """Funcion para invertir el texto ingresado, donde las mayusculas pasan a ser minisculas y las minisculas, mayusculas"""
    texto_inv = ''
    for i in range(0,len(texto)):
        if texto[i].islower():
            texto_inv = texto_inv + texto[i].upper()
        elif texto[i].isupper():
            texto_inv = texto_inv + texto[i].lower()
        else:
            texto_inv = texto_inv +  texto[i]
    return texto_inv
                        
   

def prueba():
    texto = input("Ingrese el texto a invertir: ")
    print("El texto invertido: ",inversion(texto))

if __name__ == "__main__":
    prueba()


