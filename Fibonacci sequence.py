# Fibonacci sequence 
l=0
c=0
c1=1
fib= str(c) +","+ str(c1)
print("\nFibanocci Sequence Program \n--------------------------")
a=input("Enter number of digits requried for the sequence : ")
a=int(a)
while l<a-2:
    n=c+c1
    c=c1
    c1=n
    fib+=","+ str(n)
    l+=1
print (fib)