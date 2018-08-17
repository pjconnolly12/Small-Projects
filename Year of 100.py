#What year will you be 100??

def what_year(name, age, copies):
    for i in range(copies):
        year = (100 - int(age)) + 2018
        string = 'Hello ' + name + ', you will be 100 in the year ' + str(year) + '!'
        print(string)

name = input('What is your name? ')
age = input('How old are you? ')
what_year(name, age, 3)
