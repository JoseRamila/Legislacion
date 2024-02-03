# Cifrado Fernet

# Importamos Fernet
from  cryptography.fernet import Fernet

# Generamos la clave
clave = Fernet.generate_key()

# Creamos la instancia Fernet
f = Fernet(clave)

# Encriptamos el mensaje
token = f.encrypt(b'El Rasho desde que trabaja en Accenture es muy agrandado xD')

# Mensaje Cifrado
print(token)

# Descifrar
#des = f.decrypt(token)

#print(des)


