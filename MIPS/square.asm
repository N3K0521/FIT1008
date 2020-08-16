.data
 	prompt: .asciiz "Input integer to square: "
	number: .word 0
	square: .word 0

.text
	#print prompt
	la $a0, prompt
	addi $v0, $0, 4
	syscall

	#read integer
	addi $v0, $0, 5 # code for reading integer
	syscall
	sw $v0, number

	#square operation
	lw $t0, number # load number
	mult $t0 , $t0 # LO = y*z
	mflo $t0 # $t1= y*z
	sw $t0, square # square = number*number

	#print result
	lw $a0, square # load square
	addi $v0, $0, 1 # code for printing integer
	syscall