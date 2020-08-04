""" Menu to read items into a list, print the list, and reverse it. """

from typing import List, TypeVar #imports some types you may need

T = TypeVar('T') # creates a type variable which you may need

def print_menu() -> None:
    print('\nMenu:')
    print('1. append')
    print('2. reverse')
    print('3. print')
    print('4. quit')

def reverse(my_list:list):
    length = len(my_list)
    for i in range(length//2):
        temp = my_list[i]
        my_list[i] = my_list[length-i-1]
        my_list[length-i-1] = temp

def last(my_list:list):
    new_list = []
    for i in range(len(list)-1):
        new_list.append(list[i])
        i += 1

my_list = []
selected_quit = False
input_line = None

while not selected_quit:
    print_menu()
    command = int(input("\nEnter command: "))
    if command == 1:
        item = input("Item? ")
        my_list.append(item)
    elif command == 2:
        reverse(my_list)
    elif command == 3:
        print(my_list)
    elif command == 4:
        last(my_list)
    elif command == 4:
        selected_quit = True
