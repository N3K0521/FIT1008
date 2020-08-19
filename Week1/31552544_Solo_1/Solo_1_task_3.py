""" Menu to operate the change of bases including from decimal to binary, hexadecimal and any other base from 2 to 16. """

__author__ = "Huixin Wang"

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

def decimal_to_other_bases(number, base):
    """
    convert number from decimal to other bases
    :raises ValueError: if the base is exceed than 16 or negative; if the number is negative
    """
    new_number = []
    if base >=1 and base < 16:
        while number > 0:
            new_number.append(int(number%base))#append the result of division to the new list
            number = number // base #divide the reminder until the result become 0
        for i in range(len(new_number)//2): #reverse the new list so the converted number can be returned
            temp = new_number[i]
            my_list[i] = new_number[len[new_number]-i-1]
            new_number[len[new_number]-i-1]
        return new_number
    else:
        return False
            
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
        number = input("Enter number to be converted ")
        base = input("Enter base to be converted to ")
        decimal_to_other_bases(number)
    elif command == 4:
        selected_quit = True