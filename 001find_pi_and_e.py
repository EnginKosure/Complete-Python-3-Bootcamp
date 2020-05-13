import math
print('Hello World!')
print('new')
print(math.pi)
print(math.e)
# Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places.
# Keep a limit to how far the program will go.
def special_pi(input):
    if input==0:
        print('pi', str(math.pi)[:input+1])
    else:
        print('pi', str(math.pi)[:input+2])




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

# Find e to the Nth Digit - Just like the previous problem, but with e instead of PI.
# Enter a number and have the program generate e up to that many decimal places.
# Keep a limit to how far the program will go.

def special_e(input):
    if input==0:
        print('e', str(math.e)[:input+1])
    else:
        print('e', str(math.e)[:input+2])

def take_input_for_e():
    while True:
        try:
            input_e=int(input('Enter a number between 0-15: '))
        except ValueError:
            print('It must be an integer!')
        else:
            if input_e<0 or input_e>15:
                print('It must be between 0-15')
            else:
                break
    return input_e

special_e(take_input_for_e())

