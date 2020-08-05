""" Menu to operate the change of bases including from decimal to binary, hexadecimal and any other base from 2 to 16. """

from typing import List, TypeVar #imports some types you may need

T = TypeVar('T') # creates a type variable which you may need

def print_menu() -> None:
    print('\nMenu:')
    print('1. Decimal to Binary')
    print('2. Decimal to Hexadecimal')
    print('3. Decimal to Other Base')
    print('4. Quit')

def decimal_to_binary(number):
    """
    convert the input number from decimal to binary
    :raises ValueError: if the number input is negative
    """
    if number > 0 and number <= 1: #if the positive integer is less than 2, its binary form is itself
        print(number)
    elif number > 1:
        decimal_to_binary(number//2) #divide number by 2, take the reminder and start again until the result is 0
        print(number%2) 
              
def decimal_to_hexadecimal(number):
    """
    convert the input number from decimal to hexadecimal
    :raises ValueError: if the number input is negative
    """
    if number > 0 and number < 10: #if the positive integer is less than 10, its binary form is itself
        print(number)
    else:
        """
        divide number by 16, take the reminder and start again until the result is 0
        """
        decimal_to_hexadecimal(number//16)
        number = number % 16
        if number < 10:
            print(number)
        elif number == 10: #for number greater than 10, the integer will be converted into its hexadecimal form
            print("A")
        elif number == 11:
            print("B")
        elif number == 12:
            print("C")
        elif number == 13:
            print("D")
        elif number == 14:
            print("E")
        elif number == 15:
            print("F")

def decimal_to_other_bases(number, base):
    """
    convert number from decimal to other bases
    :raises ValueError: if the positive number is exceed than 16
    """
    if number > 0 and number < 16: 
        number = number % base
    else:
        number < 10
        number = (number % base) // base  
            
number = ''
selected_quit = False
input_line = None

while not selected_quit:
    print_menu()
    command = int(input("\nEnter command: "))
    if command == 1:
        number = input("Enter number to be converted ")
        base = input("Enter base to be converted to ")
        decimal_to_binary(number, base)
    elif command == 2:
        number = input("Enter number to be converted ")
        decimal_to_hexadecimal(number)
    elif command == 3:
        number = input("Enter number to be converted ")
        decimal_to_other_bases(number)
    elif command == 4:
        selected_quit = True