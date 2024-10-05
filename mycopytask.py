number = int(input("How many numbers would you like"))
numbers = []

for x in range (number):
    ask = input("number")
    numbers.append(ask)

print(numbers)

for number in numbers:
    if number > "0":
        print(number + "positive")
    elif number < "0":
        print(number + "negative")
    else:
        print()