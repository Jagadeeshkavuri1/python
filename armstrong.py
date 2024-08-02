n=int(input("enter a number "))  
a=n
sum=0
while(n>0): 
    rem=n%10
    sum=sum+rem**3
    n=n//10  
if(sum==a): 
    print("armstrong ") 
else: 
    print("not armstrong  ")  