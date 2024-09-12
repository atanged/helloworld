str='This is the first text'
print(str)
# capstr=str.upper()
# if capstr:
#     print(f'No chance {capstr}')
# else:
#     print('If block got skipped, condition was not true.')

# str1=input('What is your name? ')

# if str1.upper()!='TEST':
#     print('Name Mismatch')
# else:
#     print('Name Match')

print(str[-1])
print(str[3:6])
print(str[3:-1:2])
print(len(str))

def user(name):
    name=input('Enter you name :')
    lname=len(name)
    print(f'Lenth of name {lname}')

c=0
length=len(str)
while c<length:
    print(str[c])
    print(f"---{c}")
    c=c+1




    