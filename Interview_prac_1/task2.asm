#python code
size = int(input("Array length: "))
the_list = [None] * size

for i in range(len(the_list)): 
    the_list[i] = int(input("Enter num: "))
    if i == 0 or min_item > the_list[i]:
        min_item = the_list[i]

print("The minimum element in this list is " + str(min_item))

#mips code
.data   
prompt1: .asciiz "Array length: "
prompt2: .asciiz "Enter num: "
prompt3: .asciiz "The minimum element in this list is "
newline: .asciiz "\n"  
x: .word 0 # x was initialised to 0 in Python
z: .word 0 # no initial value provided for z, but use .word for simplicity (and alignment)
k: .word 0
y: .word 0 # y is a pointer to the array location; we do not yet know its address
i: .word 0 # variable i was not initialised in Python either
       
.text
# Printing "Array length: " 
la $a0, prompt1   
addi $v0, $0, 4   
syscall           

# read z
addi $v0, $0, 5
syscall
sw $v0, z

# Printing "Enter num: "
la $a0, prompt2
addi $v0, $0, 4
syscall
  
#read the input for prompt2
addi $v0, $0, 5
syscall
sw $v0, k

loop:
###

# if z > 0:
lw $t0, z
slt $t1, $0, $t0    # is z > 0?
beq $t1, $0, endif  # if not, go to endif

# Printing "The minimum element in this list is "
la $a0, prompt3    
addi $v0, $0, 4    
syscall            

# printing integer x
lw $a0, x          
addi $v0, $0, 1    
syscall

# Printing newline
la $a0, newline
addi $v0, $0, 4    
syscall            
endif:
# Exit the program
addi $v0, $0, 10   
syscall      