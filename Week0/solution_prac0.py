""" Possible solutions to prac0. 

Note that functions whose name starts with __ are meant to be private.
Note also that the last two lines are designed to make the module behave
like a script when called (rather than imported). This is because the 
value of variable __name__ is set by the Python interpreter. It is 
"__main__" if we run this file as the main program using for example, 
"python solution_prac0.py". If this file is however imported by another 
program, then __name__ will be set to the other program and this if-then
will fail. So, this if-then calls main() if this program is the main 
program.  

"""

__author__ = "Maria Garcia de la Banda"

from typing import List  # this is how we import things

def read_integers() -> List[int]:
    """ Reads list of integers from standard input."""
    list_strings = input("Enter some integers:").split()
    return __list_strings_to_integers(list_strings)

def __list_strings_to_integers(list_strings:List[str]) -> List[int]:
    """ Converts a list of strings into a list of integers.
    :throws: ValueError if the string are not integers 
    """
    list_integers = []
    for item in list_strings:
        list_integers.append(int(item))
    return list_integers

def sum_squared_integers(list_integers:List[int]) -> int:
    sum = 0
    for integer in list_integers:
        sum += integer**2
    return sum

def read_from_file_sum_squares() -> None:
    """ It iteratively reads the integers in each file line and 
    sums its integers squared.
    """
    list_lines = __read_from_file()
    for line in list_lines:
        list_strings = line.split()
        list_integers = __list_strings_to_integers(list_strings)
        print(sum_squared_integers(list_integers))

def __read_from_file() -> List[str]:
    """ Reads the lines of a file into a list of lines and returns it."""
    filename = input("Enter the filename:")
    file = open(filename, "r")
    list_lines = file.readlines()
    file.close()
    return list_lines

def read_from_file_table() -> None:
    """ Converts the file lines into a list of list of integers.
    :throws: ValueError if the lines are not integer sequences 
    """
    list_lines = __read_from_file()
    table = []
    for line in list_lines:
        list_strings = line.split()
        list_non_negatives = []
        for item in list_strings:
            integer = int(item)
            if integer >= 0:
                list_non_negatives.append(integer)
        table.append(list_non_negatives)
    print(table)

def main():
    """ Calls all functions defined above."""
    list_integers = read_integers()
    print(list_integers)
    sum = sum_squared_integers(list_integers)
    print(sum)
    read_from_file_sum_squares()
    read_from_file_table()

if __name__ == "__main__":
    main()
