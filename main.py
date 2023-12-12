import sympy

# custom implementation for exponentiation of numbers
def customPow(base, exponent, modulus = None):
    if modulus is None:
        result = 1
        for _ in range(exponent):
            result *= base
        return result

    if base > modulus:
        base = base % modulus

    result = 1
    while exponent > 0:
        # check if LSB(least significant bit) bit is 1 and do multiplication
        if exponent % 2 == 1: 
            result = (result * base) % modulus

        base = (base * base) % modulus
        # shift all bits to right 
        # to check LSB bit in next loop
        exponent //= 2
    return result

def checkSignIsValid(sign, e, n, realMessage):
    newMessage = customPow(sign, e, n)
    print('newMessage', newMessage)
    print('*********************************************')
    return realMessage == newMessage

def generateE(phiN):
    e = sympy.randprime(2, phiN)
    while sympy.gcd(e, phiN) != 1:
        e = sympy.randprime(2, phiN)

    return e

def generateD(e,phiN):
    d = sympy.mod_inverse(e, phiN)
    while (e * d) % phiN != 1:
        d = sympy.mod_inverse(e, phiN)
    return d

message = input('Enter your message (number & decimal format): ')
MIN_PRIME_RANGE = input('Enter minimum prime range for produce prime number(default is: 1024): ')
MAX_PRIME_RANGE = input('Enter maximum prime range for produce prime number(default is: 2048): ')

if message == '':
    raise Exception("Sorry, no messages provided from you")
else:
    message = int(message)

if MIN_PRIME_RANGE == '':
    MIN_PRIME_RANGE = 1024
else:
    MIN_PRIME_RANGE = int(MIN_PRIME_RANGE)

if MAX_PRIME_RANGE == '': 
    MAX_PRIME_RANGE = 2048
else:
    MAX_PRIME_RANGE = int(MAX_PRIME_RANGE)

# produce two random prime number
p = sympy.randprime(MIN_PRIME_RANGE, MAX_PRIME_RANGE)
q = sympy.randprime(MIN_PRIME_RANGE, MAX_PRIME_RANGE)
n = p * q

# this formula for phi(N) only works for prime number
# for other numbers we should use another approach
phiN = (p - 1) * (q - 1) 

e = generateE(phiN)
d = generateD(e,phiN)
sign = customPow(message, d, n)

print('message',message)
print('*********************************************')
print('valid',checkSignIsValid(sign,e,n,message))