import random
import hashlib


# Parámetros Diffie-Hellman
p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919
g = 2

# Generación de llaves privadas aleatorias
alice_private_key = random.randint(0, p)
bob_private_key = random.randint(0, p)  
eve_private_key = random.randint(0, p)

# Intercambio de claves públicas
alice_public_key = pow(g, alice_private_key, p)
bob_public_key = pow(g, bob_private_key, p)
eve_public_key = pow(g, eve_private_key, p)

# Cálculo de llaves compartidas
alice_eve_key = pow(eve_public_key, alice_private_key, p)
bob_eve_key = pow(eve_public_key, bob_private_key, p)

print("Llave compartida Alice-Eve:", alice_eve_key)
print("Llave compartida Bob-Eve:", bob_eve_key)

# Intercambio de mensajes
message_a = "Hola Bob, soy Alice"  
message_b = "Hola Alice, aquí Bob"

print("Mensaje de Alice:", message_a)
print("Mensaje interceptado por Eve:", message_a) 

print("Mensaje de Bob:", message_b)
print("Mensaje interceptado por Eve:",message_b)