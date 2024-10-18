class a:  
    def add(self,x,y): 
        print("addition is ",(x+y)) 
class b(a): 
    def sub(self,x,y): 
        print("subtraction is ",(x-y)) 
class c(b): 
    def mul(self,x,y): 
        print("multiplication is",(x*y)) 
class d(c): 
    def div(self,x,y): 
        print("floor division",(x/y)) 
f=d() 
x=int(input("enter x value")) 
y=int(input("enter y value ")) 
print("x values is",x,"y values is",y) 
f.add(x,y) 
f.sub(x,y) 
f.mul(x,y) 
f.div(x,y) 
           