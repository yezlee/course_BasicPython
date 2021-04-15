class Animal:
    def __init__(self):
        self.age =0
        self.egg = False
    def getOld(self):
        self.age+=1
    def chageEgg(self):    
        self.egg = not self.egg
        
        
class Human(Animal):
    def __init__(self):
        super().__init__()
#         Animal.__init__(self)
        self.moneypower = 11
    def makeMoney(self,earnmoney):
        self.moneypower += earnmoney
        
   


a = Human()
print(a.age)
print(a.egg)
print(a.moneypower)

a.getOld()
a.chageEgg()
a.makeMoney(100)
print(a.age)
print(a.egg)
print(a.moneypower)
