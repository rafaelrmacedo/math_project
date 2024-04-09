import math

senha = input("Qual a sua senha? ")


def criptografar(x):
    return x ** 2 + 2 * x


def representar_em_ASCII(x):
    return ord(x)


senha_ascii = list(map(representar_em_ASCII, senha))
senha_cripto = list(map(criptografar, senha_ascii))