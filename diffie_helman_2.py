import random
import hashlib


# Parámetros Diffie-Hellman
p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919
g = 2

# Generación de llaves privadas aleatorias
a_p_k = random.randint(0, p)
b_p_k = random.randint(0, p)  
e_p_k = random.randint(0, p)

# Intercambio de claves públicas
alice_public_key = pow(g, a_p_k, p)
bob_public_key = pow(g, b_p_k, p)
eve_public_key = pow(g, e_p_k, p)

# Cálculo de llaves compartidas
alice_eve_key = pow(eve_public_key, a_p_k, p)
bob_eve_key = pow(eve_public_key, b_p_k, p)

print("Llave compartida Alice y Eve:", alice_eve_key)
print("Llave compartida Bob y Eve:", bob_eve_key)

# Intercambio de mensajes
m_a = "Hola Bob, soy Alice"  
m_b = "Hola Alice, soy Bob"

print("Mensaje de Alice:", m_a)
print("Mensaje interceptado por Eve:", m_a) 

print("Mensaje de Bob:", m_b)
print("Mensaje interceptado por Eve:",m_b)