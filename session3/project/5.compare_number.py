firstNumber = int(input("Enter first number to comparing: "))
secondNumber = int(input("Enter second number to comparing: "))

if firstNumber > secondNumber:
    print(firstNumber, "is greater than", secondNumber)
elif firstNumber < secondNumber:
    print(firstNumber, "is less than", secondNumber)
elif firstNumber == secondNumber:
    print(firstNumber, "is equal to", secondNumber)