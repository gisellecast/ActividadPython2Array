#arreglo suma py

import random
def SumaArreglo(x):
    arreglo = [ ]
    for i in range (x):
        arreglo.append(random.randint(1,1000))
    return arreglo, sum(arreglo)

arreglosuma, suma = SumaArreglo(3)
print("El arreglo es: ")
print(arreglosuma)

print("La suma del arreglo es " + str(suma))
