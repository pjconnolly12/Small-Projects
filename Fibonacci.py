# Fibonacci (Non-Recursive)

def f(num):
    first = 0
    second = 1
    for i in range(0,int(num/2)):
        print(first)
        print(second)
        first += second
        second += first
        
#Fibonacci (Recursive)

def recursive(num):
    if num == 0 or num == 1:
        return num
    else:
        return recursive(num - 1) + recursive(num - 2)


#Fibonacci (Recursive) (Print all function)

def print_fib(num):
    for i in range(0,num + 1):
        print(recursive(i))

print_fib(34)


    
