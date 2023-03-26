import math


def isprime(n):
    # a funtion to check whether
    #  the number is prime or not
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True


def primefactors(n):
    # a function which return all
    # pair of prime factors of a number2
    factors = []
    for i in range(n):
        if isprime(i):
            if n % i == 0:
                fac = int(n/i)
                if isprime(fac):
                    factors.append((i, fac))
    return factors


pubk = input('\n\nEnter Public Key : ').split(',')

n = int(pubk[1])

cipher = input('Enter the cipher number : ').split(',')
for i in range(len(cipher)):
    cipher[i] = int(cipher[i])

factors = primefactors(n)

print('\nPrime Factors found : ', factors)

for k in factors:
    print('\n\nDecryption using prime factors : ', k)

    if len(k) == 2:
        # assigning the prime factors value to p and q
        p = k[0]
        q = k[1]

        fi_p = p - 1
        fi_q = q - 1

        # calculating n - should not be prime and number of prime factors of it
        n = p*q
        fi_n = fi_p * fi_q

        # assigning e using public key
        e = int(pubk[0])
        d = 0

        # calculating d for given e
        for d in range(fi_n):
            d += 1
            if ((e*d) % fi_n) == 1:
                break

        if e*d % fi_n == 1:
            print('For e :', e, 'found d :', d)
        else:
            print('Using prime factors', k, 'for e :', e, 'd not found')
            continue
            if k == factors[len(factors) - 1]:
                exit(0)

        print('Cipher to decrypt : ', cipher)
        plain = []

        for i in cipher:
            plain.append((i**d) % n)

        print('Decrypted plain numbers : ', plain)
        print('Decrypted message : ', end='')

        for i in plain:
            print(chr(i), end='')
        print('')
