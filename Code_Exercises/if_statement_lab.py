#example of if statement

try:
    userInputString = input("Enter a number: ")
    number = int(userInputString)

    if (number < 0):
        print("You enter a positive number " + str(number))
    elif (number > 0):
        print("You enter a positive number " + str(number))
    else:
        print("You enter in 0 (zero)")

except ValueError:
    print("No valid number")