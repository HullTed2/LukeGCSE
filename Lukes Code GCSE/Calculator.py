# Calculator

number1 = int(input('Enter First number: '))

print("""
Choose one of the following options:
A for Add
S for Subtract
M for Multiply
D for Divide""")

operator = input()

number2 = int(input('Enter second number: '))

if operator == 'A' :
    print (number1 + number2)
elif operator == 'S' :
    print (number1 - number2)
elif operator == 'M' :
    print (number1 * number2)
elif operator == 'D' :
    print (number1 / number2)
else:
    print('Incorrect Operator')
