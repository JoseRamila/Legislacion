import random
import hashlib

# Paso 1: Investigar número primo p (puede sustituirse por otro primo)
p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919  # Número primo de 256 bits

# Paso 2: Generar llaves privadas aleatorias para A y B
a = random.getrandbits(256)
b = random.getrandbits(256)

# Paso 3: Simular intercambio de números entre A y B
public_key_a = pow(2, a, p)  
public_key_b = pow(2, b, p)  

# Paso 4: Calcular la llave secreta "s"
secret_key_a = pow(public_key_b, a, p)  
secret_key_b = pow(public_key_a, b, p)  

# Verificar que las llaves secretas sean iguales usando SHA-256
hash_a = hashlib.sha256(str(secret_key_a).encode()).hexdigest()
hash_b = hashlib.sha256(str(secret_key_b).encode()).hexdigest()

# Imprimir resultados
print("Número primo (p):", p,"\n")

print("Llave privada de Alice (A):", a,"\n")
print("Llave privada de Bob (B):", b,"\n")
print("Llave pública de Alice (g^A mod p):", public_key_a,"\n")
print("Llave pública de Bob (g^B mod p):", public_key_b,"\n")
print("Llave secreta de Alice (g^B^A mod p):", secret_key_a,"\n")
print("Llave secreta de Bob (g^A^B mod p):", secret_key_b,"\n")
print("Hash de la llave secreta de Alice:", hash_a,"\n")
print("Hash de la llave secreta de Bob:", hash_b,"\n")

# Verificar si las llaves secretas son iguales
if hash_a == hash_b:
    print("¡Las llaves secretas son iguales!""\n")
else:
    print("¡Las llaves secretas no son iguales!""\n")
