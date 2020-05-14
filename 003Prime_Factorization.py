# Prime Factorization -
# Have the user enter a number and find all Prime Factors (if there are any) and display them.

def find_primes(input):
    primes=[]
    for i in range(input+1):
        if is_prime(i):
            primes.append(i)
    print(primes)

def is_prime(num):
    '''
    Method of checking for primes.
    '''
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

input=int(input('enter a number: '))

# find_primes(input)

def blanket():
    find_primes(input)

if __name__=='__main__':
    blanket()

