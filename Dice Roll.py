from random import randint

x = "y"
while x == "y":
    print(randint(1, 6))
    x = input("Would you like to roll again? (y/n)")

