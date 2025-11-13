'''
    Simple Calculator with Match Case
'''

# Prompts for User Input
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

op = input('Choose the operation (+, -, *, /): ')

# Perform the Calculation Using Match Case
match op:
    case '+':
        result = num1 + num2
        print('The result is {}.'.format(result))
    case '-':
        result = num1 - num2
        print('The result is {}.'.format(result))
    case '*':
        result = num1 * num2
        print('The result is {}.'.format(result))
    case '/':
        if num2 == 0:
            print('Cannot divide by zero.')
        else:
            result = num1 / num2
            print('The result is {}.'.format(result))
