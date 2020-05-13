import math
print('Hello World!')
print('new')
print(math.pi)
print(math.e)
# Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places.
# Keep a limit to how far the program will go.
def special_pi(input):
    if input==0:
        print(str(math.pi)[:input+1])
    else:
        print(str(math.pi)[:input+2])




# user_input =0


def take_input():

    while True:
        try:
            user_input = int(input('Select a number (between 0-15) for the length after comma: '))
        except ValueError:
            print('Sorry, it must be an integer!')
        else:
            if user_input > 15 or user_input<0:
                print("Sorry, your input must be between 0-15")
            else:
                break
    return user_input

special_pi(take_input())

