# Prime Factorization -
# Have the user enter a number and find all Prime Factors (if there are any) and display them.


def find_primes(inp):
    primes = []
    for i in range(inp + 1):
        if is_prime(i):
            primes.append(i)
    print(primes)


def is_prime(num):
    """
    Function for checking primes.
    """
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


input1 = int(input('enter a number: '))


# Next Prime Number -
# Have the program find prime numbers until the user chooses to stop asking for the next one.


def find_prime_one_by_one(num):
    """
    Finds primes asking user each time
    """
    if is_prime(num):
        print('Next prime number is :', num)
        return True
    else:
        # print('it is not prime')
        return False


def take_input():
    x = 2
    find_prime_one_by_one(x)
    while True:
        next1 = input('find next prime number? enter y or n ')

        if next1 and next1[0].lower() == 'y':
            x += 1
            while not find_prime_one_by_one(x):
                x += 1
        else:
            print("See you later!")
            break
    return next1


def blanket():
    find_primes(input1)


if __name__ == '__main__':
    blanket()
    print('First func executed, now the second')
    take_input()
