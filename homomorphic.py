import math
import random


def gcd(a, b):
    # gcd funtion to get greatest common
    # divisor between 2 numbers
    num = min(a, b)
    while num:
        if a % num == 0 and b % num == 0:
            break
        num -= 1
    return num


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


# choosing 2 prime numbers p, q and their number of prime factors
p, q = 4, 4
while not isprime(p):
    p = random.randint(1, 100)

while not isprime(q):
    q = random.randint(1, 100)

print('\n\nHomomorphic Encryption using RSA')

print('\np :', p, 'and q :', q, ' found')

fi_p = p - 1
fi_q = q - 1

# calculating n - should not be prime and number of prime factors of it
n = p*q
print('n :', n, 'found')
fi_n = fi_p * fi_q

# calculating e and d
e = 0
d = 0
while e*d % fi_n != 1:
    # initialise e randomly between
    # half fi_n to fourth fi_n
    e = random.randint(fi_n/4, fi_n/2)  # math.ceil(fi_n/2)

    # check if the gcd of
    # n and e is 1
    # if true calculate g
    # else change value of e
    # till not 1
    while e < fi_n:
        if gcd(e, n) == 1:
            break
        e -= 1

    # calculating d
    # if d and e are nultiplicative inverse then stop
    # else loop till fi_n
    for d in range(fi_n):
        d += 1
        if ((e*d) % fi_n) == 1:
            break

if e*d % fi_n == 1:
    print('e :', e, 'and d :', d, ' found')
else:
    print('e and d not found')
    exit(0)

pubk = (e, n)
prvk = (d, n)

print('Public Key :', pubk)
print('Private Key :', prvk)


message1 = int(input('\n\nEnter the message 1 to encrypt : '))
message2 = int(input('Enter the message 2 to encrypt : '))
message3 = message1 * message2

encyp1 = pow(message1, e, n)
encyp2 = pow(message2, e, n)
encyp3 = pow(message3, e, n)

# print('Encrypted Messages : ', encyp1, encyp2, encyp3)

print('\nCipher 1 :', encyp1)
print('Cipher 2 :', encyp2)
print('cipher 3 :', encyp3)
print('\n(c1 * c2)%n = ', (encyp1*encyp2)%n)

if encyp3 == (encyp1 * encyp2)%n:
    print('\nHomomorphic Encryption Multiplicative Property Satisfied.\n')
else:
    print('\nHomomorphic Encrytion Multiplicative Property not Statisfied\n.')

message3 = message1 + message2

encyp1 = pow(message1, e, n)
encyp2 = pow(message2, e, n)
encyp3 = pow(message3, e, n)

# print('Encrypted Messages : ', encyp1, encyp2, encyp3)

print('\nCipher 1 :', encyp1)
print('Cipher 2 :', encyp2)
print('cipher 3 :', encyp3)
print('\n(c1 + c2)%n = ', (encyp1+encyp2)%n)

if encyp3 == (encyp1 + encyp2)%n:
    print('\nHomomorphic Encryption Multiplicative Property Satisfied.\n')
else:
    print('\nHomomorphic Encrytion Multiplicative Property not Statisfied\n.')

