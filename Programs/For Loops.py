#Program using For loop
o="Y"
while o!="X":
    o=input("\n\nEnter options: \n1.Range with number \n2.range with len()\nExit Program[X]\n ")
    o=o.upper()
    if o=="1": 
        for i in range(10):
            print (i)
    elif o=="2":
        z="hello"
        for j in range(len(z)):
            print(j)
    elif o!="X":
       print("Invalid Entry, Try Again") 
print("End of Program")    