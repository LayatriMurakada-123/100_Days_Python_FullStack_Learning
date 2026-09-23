
Polymorphism --> Method Overloading, Method Overriding, Operator Overloading

#Method Overloading --> Default arguments, variable length arguments, Type of

#Method Overloading (Compile time Polymorphism) --> Default arguments

class Hotstar:
    """default args usage"""
    def watch(self,movie=None):
        self.movie = movie
        if self.movie == None:
            print(f'Welcome to Hotstar')
        elif self.movie == movie:
            print(f'User watching {self.movie}')
u1 = Hotstar()
#u1.watch() #in this case we made movie as default
u1.watch("Vikram")

#Variable length arguments

class Hotstar:
    """default args usage"""
    def add_tolist(self,movie=None):
        print(f'Welcome to Hotstar')
    def watch(self, *movies):
        print("Movies available for you:")
        for movie in movies:
            print(movie)

u1 = Hotstar()
u1.add_tolist()
u1.watch("Vikram", "Leo", "Jailer", "Pushpa")

#Method overloading with type of arguments(isinstance())
#Hotstar --> one movie, multiple movies

class Hotstar:
    """default args usage"""
    def watch(self,movie = None):
        print(f'Welcome to Hotstar')
    def movies_list(self,content):
        self.content = content
        if isinstance(content,str):
            print(f'User watching {self.content}')
        elif isinstance(content,list):
            print(content)
            for movie in content:
                print(movie)
u1 = Hotstar()
u1.watch()
u2 = Hotstar()
u2.movies_list("Vikram")
u2.movies_list(["Leo","Vikram","BlackPanther"])
print(u2.movies_list(("Save the Tigers","Dune"))) #it returns None


#Method Overriding --> Inheritance usage
#when the same method name is used in base class and also in derived class
#super()

#Free user --> [can watch free content with advertisements]
#Premium User  --> [Can watch premium content without adviertisements]
#VIP user --> [Can watch premium content along with devices count,streaming] 

class Hotstar:
    """Method Overriding with the example of the parent class"""
    def watch(self):
        print("Welcome to Hotstar!")

class FreeUser(Hotstar):
    def watch(self):
        super().watch()
        print("Free User: Can watch free content with advertisements")

class PremiumUser(FreeUser):
    def watch(self):
        super().watch()
        print("Premium User: Can watch premium content without advertisements")

class VIPUser(PremiumUser):
    def watch(self):
        super().watch()
        print("VIP User: Can watch premium content with device count and streaming")

# Objects
u1 = FreeUser()
u2 = PremiumUser()
u3 = VIPUser()
#u1.watch()
#print()
#u2.watch()
#print()
u3.watch()


#Operator Overloading --> (Magic methods/dunder methods) __init__(),__add__()

a=13;b=24
print(a+b)
print(a.__add__(b)) #self.value + other.value
print('codegnan'.__add__('python')) #concatention
print([1,3,].__add__([2,34,9])) #Merging

#In above case same __add__() is performing different cases (Addition, Concatenation, merging)

a = [1,2,3,4,5]
print(a.__len()) #len(a)



#now linking above operators scenerio to Hotstar

class WatchHistory:
    """Duration of watching content"""
    def duration (self,hours):
        self.hours = hours
    def __add__(self,other):
        return self.hours + other.hours
u1 = WatchHistory()
u1.duration(25)
u2 = WatchHistory()
u2.duration(35)
print(u1.hours + u2.hours) 
#get the complete duration
print(u1+u2) #this is directly accessible when we have __add__() 

#-------------OR----------------------

class WatchHistory:
    """Duration of watching content"""
    def duration (self,hours):
        self.hours = hours
u1 = WatchHistory()
u1.duration(25)
u2 = WatchHistory()
u2.duration(35)
print(u1.hours + u2.hours) 


#3rd case using __str__ method
class WatchHistory:
    """Duration of watching content"""
    def duration(self,hours):
        self.hours=hours
    def __add__(self,other):
        return self.hours+other.hours
    def __str__(self):
        print(f'User watching {self.hours} hours duration')
u1=WatchHistory()
u1.duration(25)
u2=WatchHistory()
u2.duration(35)
#get the complete duration
print(u1+u2)
u1.__str__()
u2.__str__()







