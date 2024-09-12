# Multiplication Tables
c=1
ic=0
print("\nTables Program \n--------------")
d=input("Enter number of tables to display[1-20] : ")
d=int(d)
if d<=20:
    while c<=d:
        while ic<=12:
            product=c*ic
            print(f"{c} x {ic} = {product} ")
            ic+=1
        ic=0
        print(f"------End of table {c}------")
        c+=1
    if c<d:
        print(f" \nStarting table {c}")
    else:
        print("\nEnd of Program\n")
else: 
    print("Try again with a smaller number. Program Ended")