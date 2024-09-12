# Palindrome
print("-----------------\nPalindrome Program\n-----------------")
chk = "Y"
while chk=="Y":
    str0 = input("Enter the word or sentence to check if it is a palindrome:\n")
    l = len(str0)
    str01 = str0[-1]
    c = 2
    while c <= l:
        str01 += str0[-c]
        c +=1  
    print(f"You have entered : {str0}")
    print(f"Reverse of what you have entered : {str01}")
    if str0 == str01:
        print("Both match. This is a Palindrome.")
    else:
        print("They do not match. string you have entered is not a Palindrome.\n")
    chk = input("Do you want to check another string[Y][N]? ")
    chk = chk.upper()
print("\n--------------\nEnd of Program\n--------------")





