import random
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Longitud=int(input("Ingresa el largo de la contraseña: "))
contraseña=""

for i in range(Longitud):
    contraseña += random.choice(caracteres)

print("la contraseña es: ", contraseña)
