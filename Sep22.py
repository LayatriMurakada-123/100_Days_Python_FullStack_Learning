'''
Usage of super()
#super with arguments --> super().__init__(args)

class Father:
    """Father class with fproperty argument"""
    def __init__(self,fproperty):
        self.fproperty = fproperty
    def father_property(self):
        print(f'Father Property is {self.fproperty}')
class Kid(Father):
    """Kid class with kproperty argument"""
    def __init__(self,kproperty,fproperty):
        super().__init__(fproperty)
        self.kproperty = kproperty
    def kid_property(self):
        print(f'Kid Property is {self.kproperty}')
        print(f'Total Combined Property is {self.fproperty + self.kproperty}')
u1 = Kid(500000,250000)
u1.kid_property() #Attribute Error
u1.father_property()
print(u1.__dict__)

#MEthod Overriding --> calling superclass method

super().method()

#Calculating the areas of square,Rectangle

class Square:
    """Area of Square"""
    def __init__(self,x):
        self.x = x
    def area(self):
        print (f'Area of Square is {self.x*self.x}')
class Rectangle(Square):
    """Derived class"""
    def __init__(self,y,x):
        self.y = y
       # super().__init__(x)
    def area(self):
        print (f'Area of Rectangle is {self.x * self.y}')
obj1 = Rectangle(7,8)
print(obj1.area())
obj2 = Square(5) #as we are creating different onjects its possible
print(obj2.area())


#Multiple Inheritance - Whatsapp Scenario - Users, Bussiness Users, Premium Users

Mutliple Base classes with single dervied class

class base1:
    stmt...
    ....
class base2:
    stmt....
    ..........
class derived(base1, base2):
    stmt....
    ....


class Users:
    """Users class with basic featires"""
    def voice_call(self):
        print("User can make voice calls")
class Notifications:
    """Notifications reaching out"""
    def send_notification(self):
        print("User can get pop-up notification")
class PremiumUsers(Users,Notifications):
    """Extra feature added"""
    def verification_badge(self):
        print("User is verified and bluetick added")
u1 = PremiumUsers()
u1.verification_badge()
u1.voice_call()
print(dir(u1))


#Multilevel Inheritance - level by level

class base1:
    stmt...
    ....
class base2(base1):
    stmt....
    ..........
class base3(base2):
    stmt....
    ....

class Users:
    """USers class with base functions"""
    def send_msg(self):
        print("User can send mgs")
    def voice_call(self):
        print("Making Voice calls")
    
class BussinessUsers(Users):
    """First derived class"""
    def create_catlog(self):
        print("Details added Successfully")
        
class PremiumUsers(BussinessUsers):
    """Second Derived class"""
    def verification_badge(self):
        print("Accounts Verified")

user1 = PremiumUsers()
user1.verification_badge()
user1.create_catlog()
user1.send_msg()
user1.voice_call()

'''
#Example of Hierarchial

class Plants:
    def __init__(self, name):
        self.name = name

    def fruits(self):
        print("All Plants fruits")


class Summer(Plants):
    def __init__(self, name):
        super().__init__(name)

    def mango(self):
        print(f"The Summer Fruit is {self.name}")


class Winter(Summer):
    def __init__(self, name):
        super().__init__(name)

    def apple(self):
        print(f"The Winter Fruit is {self.name}")


u1 = Winter("Apple")
u1.mango()
u1.apple()
u1.fruits()
