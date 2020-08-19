# A simple program printing the message "I am really enjoying MIPS"
# author: Huixin Wang

.data
prompt: .asciiz "I am really enjoying MIPS \n"
newline: .asciiz "\n"

.text
main: # printing the message
la $a0, prompt # load address of string to be printed into $a0
addi $v0, $0, 4 # system call code for printing string = 4
syscall # call operating system to perform the printing operation

la $a0, newline # printing a new line
addi $v0, $0, 4 # system call code for printing string = 4
syscall # system call to perform the operation

# exit
addi $v0, $0, 10 # terminate program
syscall
