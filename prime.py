"""
prime.py -- Write the application code here
"""



def find_prime(number):
    """Finds prime factors"""
    try:
        number = int(number)
        factors = []

        while number %2 == 0:
            factors.append(2)
            number //= 2
        divisor = 3
        while number != 1 and divisor <= number:
            if number % divisor == 0:
                factors.append(divisor)
                number //= divisor
            else:
                #prime number is odd except 2
                divisor += 2

        print("the prime factors are: ")


        for i, factor in enumerate(factors):
            print(f'Prime Factor id number {i} : Prime Factor{factor}')

        return factors
    except ValueError:
        print(f'{ValueError}')
        return ValueError
