def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)    
i=int(input("enter a number "))
j=fact(i) 
print("factorial of :",i,"is",j)