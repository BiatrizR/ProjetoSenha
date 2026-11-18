import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

comprimento = int(input("Digite o tamanho da senha: "))

senha = ""


for i in range(comprimento):
    caractere = random.choice(caracteres)
    senha += caractere

print("Sua nova senha é:", senha)
