'''import math as k 
a=k.gcd(0,0) 
print(a)'''  
def gcd(a,b):
    if(b==0):
     return a
    else: 
        return gcd(b,a%b) 
a= int(input("enter a number "))
b=int(input("entera number ")) 
if(a==0 and b==0):
    print("gcd is  0") 
else:
    print(gcd(a,b))    
