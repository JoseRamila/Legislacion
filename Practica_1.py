
from Crypto.Util import number
import random 

# Ejercicio 1
print("Ejercicio 1 - Número aleatorio de 256 bits", "\n", random.getrandbits(2056), "\n")


# Ejercio 2
# Obtener un número primo
i = 0
while(True):
    i = i +1
    j = random.getrandbits(1024)
    esPrimo = number.isPrime(j)
    if(esPrimo):
        print("En la iteración: ", i, " se encontró el primo: ", j, "\n")
        break


# Ejercicio 3 
# Obtener inverso multiplicativo 
def inversoMultiplicativo(x,y):
    print("Ejercicio 3 - El inverso multiplicativo del número x: ", "\n", x, "\n", "y el número y: ", "\n", y, "\n", "es ", "\n", number.inverse(x,y), "\n")
    
    
a = random.getrandbits(1024)
b = random.getrandbits(1024)

inversoMultiplicativo(a,b)


# Ejercicio 4
# Potencia de un número 2^(e) mod p, donde "e" es un número de 256 bits y "p" es un primo de 1024 bits
a = 2
b = random.getrandbits(256)
c = j

def potencia(x,y,z):
    print("Ejercicio 4- La potencia de x a la y mod z es: ", "\n", pow(x,y,z))

potencia(a,b,c)
