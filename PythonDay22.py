'''

                             -: Inheritance :-
                                ===========

--> Inheritance is an OOP concept where one class (child/derived) acquired the properties and methods of another class (parent/base)

Syntax:-
------
class parent:
    pass
class child(parent):
    pass

1. Single inheritance:
   ------ -----------
--> A child class inherits from one parent is single inheritance

Ex:-
---
#1.single Inheritance
class animal:
    def sound(self):
        print('Animal make sounds')
class dog(animal):
    def barks(self):
        print("Dog barks")
d = dog()
d.sound()
d.barks()

#2.Single Inheritance
class father:
    def land(self):
        print('5 acre of land')
class son(father):
    def flat(self):
        print('3BHK flat')
s = son()
s.land()
s.flat()


2. Multiple Inheritance:-
   -------- -----------
--> A child inherits more than one parent is called

Ex:-
---
class father:
    def skills(self):
        print('Driving')
class mother:
    def talent(self):
        print('cooking')
class sister:
    def learn(self):
        print('python')
class son(father,mother,sister):
    def mine(self):
        print('coding')
all_ = son()
all_.skills()
all_.talent()
all_.learn()
all_.mine()


3. Multi-level Inheritance:-
   ----- ----- -----------
--> One child class becomes the parent for another class

Ex:-
--
class grandfather:
    def house(self):
        print('Owns House')
class father(grandfather):
    def flat(self):
        print("New 3BHK flat")
class son(father):
    def car(self):
        print('Have a car')
fam = son()
fam.house()
fam.flat()
fam.car()


4. Hierarchical Inheritance:-
   ------------ -----------
--> Multiple childs inherits from the same parent.

Ex:-
--
class mother:
    def gold(self):
        print('10 KG gold')
class pinky(mother):
    def show(self):
        print('will get 5kg gold')
class yuktha(mother):
    def show_2(self):
        print('will get remaining 5kg gold')
child_1 = pinky()
child_2 = yuktha()

child_1.gold()
child_1.show()

child_2.gold()
child_2.show_2()


Hybrid Inheritance:-
------ -----------
--> This is the combination of two or more types of inheritance example of multiple + multi-level

Ex:-
--
class A:
    def method_A(self):
        print('Class A')
class B(A):
    def method_B(self):
        print('Class B')
class C(A):
    def method_C(self):
        print('class C')
class D(B,C):
    def method_D(self):
        print('Class D')
S = D()
S.method_A()
S.method_B()
S.method_C()


Super():-
------
--> This Super() function is used to access the parent class methods or constructor in the child class...

Ex:-
--
#1.

class parent:
    def show(self):
        print('parent method')
class child(parent):
    def show(self):
        super().show()
        print('child class')
chi_ = child()
chi_.show()

#2.
class person:
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
        print(self.name)
        print(self.roll)
an = student('Laya',666)
an.display()



































































































































