#1
print(range(1,10))#that means only range can not do anything on itself ; has to be used in conjunction with other functions
for number in range(1 , 11 ):
    print(number)
for number in range(1,11,3):
        print(number)
#2
#Gauss challenge
total = 0
for number in range(1,101):
    total += number
print(total)
#3
#quiz
for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
