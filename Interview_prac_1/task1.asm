#python code:
first = int(input("Enter first: "))
second = int(input("Enter second: "))

if first > 0 and second >= 0:
    result = second // first
elif first == second or first < second: 
    result = first * second
else:
    result = second * 2
    
print("Result: " + str(result))

#mips code
.data
prompt1: .asciiz "Enter first: "
prompt2: .asciiz "Enter second: "
prompt3: .asciiz "Result: "
newline: .asciiz "\n"

.text
main:
#printing prompt1
la $a0, prompt1 # load address of string to be printed into $a0
addi $v0, $0, 4 # system call code for printing string = 4
syscall # call operating system to perform the printing operation
  
#read the input for prompt1
li $v0, 5
syscall
move $t1, $v0
  
#printing prompt2
la $a0, prompt2
addi $v0, $0, 4
syscall
  
#read the input for prompt2
li $v0, 5
syscall
move $t2, $v0
  
if:
bgt $t1,0, cond2
elif:
beq $t1, $t2, elifblock
blt $t1, $t2, elifblock
else:
mul $t3, $t2, 2
b print

cond2:
bge $t2, 0, ifblock
b elif

ifblock:
div $t2, $t1
mflo $t3 #because of integer division
b print
elifblock:
mul $t3, $t1, $t2
b print

print:
#printing prompt3
la $a0, prompt3
addi $v0, $0, 4
syscall

#printing the result
move $a0, $t3
li $v0, 1
syscall

#printing newline
la $a0, newline
addi $v0, $0, 4
syscall

exit:
addi $v0, $0, 10 # terminate program
syscall