sum = 0
counter = 0

number = int(input("Enter a number: "))

while number != -1:

    sum += number

    counter += 1

    average = sum / counter

    print("Running average:", average)

    number = int(input("Enter another number: "))

print("Program ended.")
