import math

from crypto import prime_pass, pub_key

pub_key = pub_key.split("JIRG")


def uncrypt_primes(prime_pass, pub_key):
    for i in pub_key:
        if i != '':
            prime_pass = prime_pass.replace(i, '-')
    return prime_pass.split('-')


def uncrypt_func(crypto_pass):
    uncryto_pass = []
    for i in crypto_pass:
        uncryto_pass.append(math.sqrt(int(i) + 1) - 1)
    return uncryto_pass


def uncrypt_ascii(uncrypto_pass):
    uncrypto_ascii = ''
    for i in uncrypto_pass:
        uncrypto_ascii += chr(int(i))
    return uncrypto_ascii


prime_uncrypto = uncrypt_primes(prime_pass, pub_key)
pass_uncrypto = uncrypt_func(prime_uncrypto)
pass_original = uncrypt_ascii(pass_uncrypto)

print(pass_original)