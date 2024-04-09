import math

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cripto import senha_cripto


def generate_primes(num_primos, bits):
    primes = []
    while len(primes) < num_primos:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=bits,
            backend=default_backend()
        )
        prime_number = private_key.public_key().public_numbers().n
        primes.append(prime_number)
    return primes


prime_numbers = []

if __name__ == "__main__":
    num_primos = len(senha_cripto) - 1  # Número de primos que desejamos gerar
    bits = 1024  # Tamanho do número primo em bits
    prime_numbers = generate_primes(num_primos, bits)


final_var = ""


print(f"\n{senha_cripto}")

for idx, number in enumerate(senha_cripto):
    final_var += str(number)
    if idx < len(prime_numbers):
        final_var += str(prime_numbers[idx])

novo_texto = ""

for number in prime_numbers:
    string_number = str(number)
    print(string_number)
    final_var = final_var.replace(string_number, "-")

final_array = final_var.split("-")

print(f"\nSenha: {final_array}")


def descriptografar(x):
    return chr(int(math.sqrt(x + 1) - 1))


def senha_numero(x):
    return int(x)


senha_numero = list(map(senha_numero, final_array))

senha_uncripto = list(map(descriptografar, senha_numero))

senha_final = ""

for caractere in senha_uncripto:
    senha_final += caractere

print(senha_final)