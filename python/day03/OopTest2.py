class Dog:
    def __init__(self):
        self.bark = True
    def muse(self):
        self.bark = False

class Bird:
    def __init__(self):
        self.flypower = 100
    def powerUp(self):    
        self.flypower += 10
        
class GaeSae(Dog,Bird):
    def __init__(self):
        Dog.__init__(self)
        Bird.__init__(self)
   
   
if __name__ == '__main__':
    
    a= GaeSae()
    print(a.bark)
    print(a.flypower)

    a.muse()
    a.powerUp()

    print(a.bark)
    print(a.flypower)



