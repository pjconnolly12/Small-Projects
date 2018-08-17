x = 1
while x <= 100:
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
        x += 1
    else:
        if x % 3 == 0:
            print("Fizz")
            x += 1
        else:
            if x % 5 == 0:
                print("Buzz")
                x += 1
            else:
                print(x)
                x += 1
