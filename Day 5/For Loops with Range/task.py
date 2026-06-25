# Range function with For Loop

for number in range(1, 10):
    print(number)

for number in range(1, 10, 3):
    print(number)


# To add every number between 1 and 100
total = 0
for number in range(1, 101):
    total += number
print(total)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)