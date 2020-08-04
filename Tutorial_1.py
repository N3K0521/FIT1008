# Tutorial 1

def is_palindrome(palindrome):
    for i in range(len(palindrome)//2):
        if palindrome[i] == palindrome[len(palindrome-i-1)]:
            continue
        else:
            return False
    return True

def is_palindrome(lst):
    n = len(lst)
    for i in range(n/2):
        if lst[x] != lst[n-1-i]:
            return False
    return True

def is_palindrome(str):
    compare = ""
    for i in range(len(string)):
        compare = string[i] + compare
    print(compare)
    return compare == string

def rever_integer(num) -> int:
    res = 0
    while num != 0:
        rem = num % 10
        num = num // 10
        res = 10*res + rem
    return res
