from sympy import randprime

password = 'teste123'


def ascii_pass(password):
    ascii = []
    for x in password:
        ascii.append(ord(x))
    return ascii


def crypto_func(ascii):
    crypto_pass = []
    for x in ascii:
        crypto_pass.append(x ** 2 + 2 * x)
    return crypto_pass


def generate_primes(crypto_pass):
    pub_key = ''
    for i in range(len(crypto_pass)):
        pub_key += 'JIRG'
        pub_key += str(randprime(2 ** (1024 - 1), 2 ** 1024))
    return pub_key


def pass_primes(pub_key):
    prime_pass = ''
    primes = pub_key.split('JIRG')
    for idx, char in enumerate(crypto_pass):
        prime_pass += str(char)
        if idx < len(primes) - 2:
            prime_pass += primes[idx + 1]
    return prime_pass


ascii = ascii_pass(password)
crypto_pass = crypto_func(ascii)
pub_key = generate_primes(crypto_pass)
prime_pass = pass_primes(pub_key)
print(password)