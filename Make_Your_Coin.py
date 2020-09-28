# Project 9 : Make your own coin
# Description: It is program explaining the OOPS concepts of class, object, constructor, destructor.
#It creates coin with respect to pound class and make the changes with the help of functions defiened
# Class is the template with the states and behaviour of object type
# Object is the instance of the class
class Pound:
    
    value=1.00
    colour="gold"
    diameter=1.5 #cm

    def rust(p):
        p.colour="green"

coin1=Pound()
coin2=Pound()
print(type(coin1)) #gives type as class
print(coin1.value)
coin1.value=1.4     #we have assigned a new value
print(coin1.value)  # this new value will be only for that specific object
print(coin2.value)
coin1.rust()
print(coin1.colour)


class Pound2:
    def __init__(self,rare=False):      #Constructor

        self.rare=rare
        if self.rare:
            self.symbol="tails"             
        else:
            self.symbol = "heads"

        self.colour="gold"
        self.diameter=1.12 #cm
    def __del__(self):                  #Destructor
        print("coin spent")
        
    def rust(self):     
        self.colour="green"
    def clean(self):
        self.colour="gold"
           
        
coin1=Pound2(rare=True)     #We can give the arguments with class name if we have constructor
print(coin1.symbol)
coin4=Pound2()
print(coin4.symbol)
coin1.rust()
print(coin1.colour)
coin1.clean()
print(coin1.colour)
coin5=Pound2()
del coin5
print(coin5.colour)     #it shows not defined since it is destructed
    
