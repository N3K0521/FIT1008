.data
integer1: .word 0
integer2: .word 0
q: .word 0
r: .word 0
prompt1: .asciiz "Please enter the first integer: "
prompt2: .asciiz "Please enter the second integer: "
quotient_prompt: .asciiz "The quotient is "
remainder_prompt: .asciiz "The remainder is "
newline: .asciiz "\n"

.text
la $a0, prompt
addi $v0, $0, 4
syscall

addi $v0, $0, 5 # printing the first integer
syscall
sw $v0, integer1

addi $v0, $0, 5 # printing the second integer
syscall
sw $v0, integer2

lw $t0, integer1 # calculating the quotient
lw $t1, integer2
div $t0, $t1
mflo $t2
sw $t2, q

lw $t0, integer1 # calculating the remainder
lw $t1, integer2
div $t0, $t1
mfhi $t2
sw $t2, remainder

lw $a0, quotient # printing the quotient
addi $v0, 1
syscall

la $a0, newline # printing a new line
addi $v0, $0, 4
syscall

lw $a0, remainder #printing the remainder
addi $v0, 1
syscall

la $a0, newline # printing a new line
addi $v0, $0, 4
syscall

# exit
addi $v0, $0, 10 # terminate program
syscall