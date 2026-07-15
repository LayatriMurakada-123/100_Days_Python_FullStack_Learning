'''
        -: OOPS :-
           ----

--> Object Oriented Programming system(OOPs), This will be organizes the code using classes and objects...

Use:-
---
--> Code reusable
--> Easy maintance
--> Clear understanding
--> Better Security


Classes:-
=======
--> Class is a blue-print or a template used to create an object...

Ex:
--
class Batch_4:
    pass


Object:-
======
--> Object is a instance of the class

Ex:
--
class student:
    studn = 'Teja'
st_ = student()
print(st_)
    

Attributes:-
==========
--> Attributes are the variable that belongs to an object or the class

Ex:
--
class how:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def nam(self):
        print(self.name)
s1 = how('Laya',22)
print(s1.nam())


Methods:-
=======
--> Methods are nothing but, the functions inside the class


'''
class calculator:
    def add(self,num,num_2):
        print(num + num_2)
    def sub(self,num,num_2):
        print(num - num_2)
cal = calculator()
cal.add(45,6)
cal.sub(45,6)



























