num = int(input('Enter a number: '))

digit = 0

while num > 0:
    num % 10 
    digit += 1
    num //= 10

print('The digits of integer is: ',digit)