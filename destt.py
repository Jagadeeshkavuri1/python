class abc: 
    def __init__(self,x,y):   
        print("object is created ")
        print(" sum of x and y is  ",(x+y))   
    def __del__(self): 
        print("object is deleted ")    

g = abc(20,30)   
print(g)  #address of the object  
del g
