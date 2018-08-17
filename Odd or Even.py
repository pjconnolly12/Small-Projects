# Odd or Even

def odd_even(num):
    if int(num) % 4 == 0:
        print('Four score and seven years ago!')
    else:
        if int(num) % 2 == 0:
            print('Even stevens!')
        else:
            print('Odd ball out')

num = input('Choose any number? ')
odd_even(num)
