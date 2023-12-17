import sympy


def custom_pow(base: int | float, exponent: int | float, modulus: int | float = None) -> int | float:
    """ Custom implementation for exponentiation of numbers """
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

def check_sign_is_valid(sign, e, n, real_message) -> bool:
    new_message = custom_pow(sign, e, n)
    print(f'New message: {new_message}')
    print('*' * 60)
    return real_message == new_message

def generate_e(phi_n) -> int | float:
    e = sympy.randprime(2, phi_n)
    while sympy.gcd(e, phi_n) != 1:
        e = sympy.randprime(2, phi_n)

    return e

def generate_d(e, phi_n) -> int | float:
    d = sympy.mod_inverse(e, phi_n)
    while (e * d) % phi_n != 1:
        d = sympy.mod_inverse(e, phi_n)
    return d

def main() -> None:
    try:
        message = input('Enter your message (must be an integer)(enter q to quit the program): ')

        if message.lower() == 'q':
            exit()
        else:
            message: int = int(message)
            
        MIN_PRIME_RANGE = input('Enter minimum prime range for produce prime number(default is: 1024): ')
        MAX_PRIME_RANGE = input('Enter maximum prime range for produce prime number(default is: 2048): ')

        MIN_PRIME_RANGE: int | float = 1024 if MIN_PRIME_RANGE == '' else int(MIN_PRIME_RANGE)
        MAX_PRIME_RANGE: int | float = 2048 if MAX_PRIME_RANGE == '' else int(MAX_PRIME_RANGE)

        # produce two random prime number
        p = sympy.randprime(MIN_PRIME_RANGE, MAX_PRIME_RANGE)
        q = sympy.randprime(MIN_PRIME_RANGE, MAX_PRIME_RANGE)
        n = p * q

        # this formula for phi(N) only works for prime number
        # for other numbers we should use another approach
        phi_n = (p - 1) * (q - 1) 

        e = generate_e(phi_n)
        d = generate_d(e, phi_n)
        sign = custom_pow(message, d, n)

        print(f'Message: {message}')
        print('*' * 60)
        print(f'Validation: {check_sign_is_valid(sign, e, n, message)}')

    except Exception as e:
        print('An error accured, message:')
        print(str(e))

    print('Running again...')
    main()


if __name__ == '__main__':
    main()
