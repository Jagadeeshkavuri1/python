def fabi(n): 
    if n<=1:
          return n
    else:
        return fabi(n-1)+fabi(n-2) 
a= int(input("enter a number ")) 
for i in range(0,a):
    print(fabi(i))        
