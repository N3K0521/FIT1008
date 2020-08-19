""" Menu to operate the change of bases including from decimal to binary. """

__author__ = "Huixin Wang"

from typing import List, TypeVar #imports some types you may need

T = TypeVar('T') # creates a type variable which you may need

def print_menu() -> None:
    print('\nMenu:')
    print('1. Decimal to Binary')
    print('2. Decimal to Hexadecimal')
    print('3. Quit')

def decimal_to_binary(number):
    """
    convert the input number from decimal to binary
    :raises ValueError: if the number input is negative
    """
    if number == 1: #if the positive integer is less than 2, its binary form is itself
        print(number)
    else:
        new_number = []
        while number > 0:
             new_number.append(int(number%2))
             number = number // 2
        print(str(new_number))
              
def decimal_to_hexadecimal(number):
    """
    convert the input number from decimal to hexadecimal
    :raises ValueError: if the number input is negative
    """
    if number >= 1 and number <= 10: #if the positive integer is less than 10, its binary form is itself
        print(number)
    else:
        """
        divide number by 16, take the reminder and start again until the result is 0
        """
        new_number = []
        while number > 0:
            new_number.append(int(number%16))
            number = number // 16
            if number == 10: #for number greater than 10, the integer will be represented as hexadecimal element
                number == "A"
            elif number == 11:
                number == "B"
            elif number == 12:
                number == "C"
            elif number == 13:
                number == "D"
            elif number == 14:
                number == "E"
            elif number == 15:
                number == "F"
        print(str(new_number))
            
number = []
selected_quit = False
input_line = None

while not selected_quit:
    print_menu()
    command = int(input("\nEnter command: "))
    if command == 1:
        number = input("Enter number to be converted ")
        decimal_to_binary(number, base)
    elif command == 2:
        number = input("Enter number to be converted ")
        decimal_to_hexadecimal(number)
    elif command == 3:
        selected_quit = True