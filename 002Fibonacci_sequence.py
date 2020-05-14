# Fibonacci Sequence -
# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.


def generate_fibonacci_sq(input):
    seq = []
    x = 1
    y = 1
    for i in range(input):
        seq.append(x)
        # z=x+y
        # x=y
        # y=z
        x, y = y, x + y

    print('nth term', seq)
    return seq


input = int(input('enter a number till 100'))


def fibonacci_till_input(input):
    seq = []
    x = 1
    y = 1

    while x < input:
        seq.append(x)
        x, y = y, x + y
    print('till input', seq)


generate_fibonacci_sq(input)
fibonacci_till_input(input)
