'''
    This script uses a for loop to print the multiplication table for a number from 1 to 10.
'''

# Prompts User for a Number
number = int(input('Enter a number to see its multiplication table: '))

# Generates and prints the multiplication table
for table in range(1, 11):
    print('{} * {} = {}'.format(number, table, number * table))
