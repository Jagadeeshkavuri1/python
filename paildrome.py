n=int(input("enter a number "))  
a=n
sum=0
while(n>0): 
    rem=n%10
    sum=sum*10+rem
    n=n//10  
if(sum==a): 
    print("paildrome ") 
else: 
    print("not paildrome ")        