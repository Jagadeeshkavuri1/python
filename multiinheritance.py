class parenta: 
    def additon(self,x,y): 
        print("addition is",(x+y)) 
class parentb:  
    def subtraction(self,x,y): 
        print("subtraction is ",(x-y)) 
class child(parenta,parentb):   
    x=100 

d=child() 
d.additon(30,20) 
d.subtraction(30,20) 
print(d.x) 


