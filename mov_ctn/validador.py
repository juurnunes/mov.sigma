
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z', 'Y', 'W']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

## Function

def valid(container):

    letra0 = False
    letra1 = False
    letra2 = False
    letra3 = False
    numero0 = False
    numero1 = False
    numero2 = False
    numero3 = False
    numero4 = False
    numero5 = False
    numero6 = False
    digitos = False

    if len(container.strip()) == 11:
        digitos = True
        
    for iletras in range(len(letras)):

        if container[0] == letras[iletras]:
            letra0 = True

        if container[1] == letras[iletras]:
            letra1 = True

        if container[2] == letras[iletras]:
            letra2 = True

        if container[3] == letras[iletras]:
            letra3 = True


    for inumeros in range(len(numeros)):

        if container[4] == numeros[inumeros]:
            numero0 = True
        
        if container[5] == numeros[inumeros]:
            numero1 = True

        if container[6] == numeros[inumeros]:
            numero2 = True
        
        if container[7] == numeros[inumeros]:
            numero3 = True
        
        if container[8] == numeros[inumeros]:
            numero4 = True

        if container[9] == numeros[inumeros]:
            numero5 = True
        
        if container[10] == numeros[inumeros]:
            numero6 = True


    if letra0 == True and letra1 == True and letra2 == True and letra3 == True and numero0 == True and numero1 == True and numero2 == True and numero3 == True and numero4 == True and numero5 == True and numero6 == True and digitos == True:
        return True
    else:
        return False
