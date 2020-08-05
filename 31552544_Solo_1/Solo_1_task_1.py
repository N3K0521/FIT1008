""" Menu to read items into a list, print the list, and reverse it. """

from typing import List, TypeVar #imports some types you may need

T = TypeVar('T') # creates a type variable which you may need

def print_menu() -> None: # printing a menu for the user to select the operations
    print('\nMenu:')
    print('1. append')
    print('2. reverse')
    print('3. print')
    print('4. last')
    print('5. count')
    print('6. quit')

def reverse(my_list:list):
    """ Reverses the inputing list.

    :pre: The list must contain elements
    :post: The list should not be modified
    :complexity: Best O(1) if only one element in the list, worst O(N**2),
                 where N is the length of list, when all are >= 0
    """
    length = len(my_list)
    for i in range(length//2):
        temp = my_list[i]
        my_list[i] = my_list[length-i-1]
        my_list[length-i-1] = temp

def last(my_list: list):
    '''
    Deletes the last element of the inputing list.
    :raises Error: if the inputs are not able to form a list
                    e.g.: the input elements are not the same types of data
    '''
    my_list = my_list[0:len(my_list)-1]
    print(my_list)

def count(my_list: list):
    '''
    Counts the number of elements in the inputing list
    '''
    print(len(my_list))

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
        last((my_list))
    elif command == 5:
        count(my_list)
    elif command == 6:
        selected_quit = True
