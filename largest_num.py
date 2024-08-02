n=int(input("enter n value :")) 
m=int(input("enter m value :")) 
q=int(input("enter q value :")) 
if(n<m): 
    if(m>q): 
        print("m is big ",m) 
    else: 
        print("q is big",q) 
else: 
    if(n<q): 
        print("q is big",q) 
    else: 
        print("n is big",n)            