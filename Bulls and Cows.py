from random import randint

answer = str(randint(1000, 9999))
guess = 0

print("Rules of the Game: Guess a number between 1000 and 9999, every number in the correct placement equals a cow, every"
      "incorrect answer equals a bull, once you have guess the number, you win!")

while guess != answer:
    bull = 0
    cow = 0
    guess = str(input("Guess a number: "))
    for i in range(0,4):
        if guess[i] == answer[i]:
            cow += 1
        else:
            bull += 1
    print("{} cows and {} bulls".format(cow, bull))
print("Congrats you win!")
