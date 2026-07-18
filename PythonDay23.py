'''

Polymorphism:-
============

--> Polymorphism means many form
--> It allows same method , function or operator to perform different tasks depending on the same object...

Types:-
-----

1.Method Overloading:-
  ------ ----------
--> Method overloading means having multiple methods with the same name but different parameters...

Ex:-
--
class Cal:
    def add(self,num,num_2=0):
        print(num + num_2)
    def add(self,num,num_2=0,num_3=0):
        print(num + num_2 + num_3)
obj = Cal()
obj.add(4,5)
obj.add(4,7,9)



2.Method Overridding:-
  ------ -----------
--> The Method overriding occurs when a child class provides its own implementation of a method already defined in its parent class... 

Ex:-
--
class animal:
    def sound(self):
        print("Animals make sounds")
class dog(animal):
    def sound(self):
        print("Dogs barks")
d = dog()
d.sound()


3.Operator Overloading:-
  -------- -----------
--> This allows operators (+,-,*) to work differently for user-defined objects...

1.__add__(+)
2.__sub__(-)
3.__mul__(*)
4.__truediv__(/)
5.__eq__() (==)
6.__It__() (<)

Ex:-
--
class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks - other.marks
s1 = student(56)
s2 = student(5)
print(s1 + s2)


Data Abstraction:-
==== ===========
--> Data Abstraction is the process of hiding implentation details and showing only the essential data to the user...

Ex:-
--
-> ATM
-> Car
-> app

Ex:-
--
#1.
from abc import ABC, abstractmethod
class parent:
    @abstractmethod
    def display(self):
        pass

#2.
from abc import ABC, abstractmethod
class bank:
    @abstractmethod
    def interest(self):
        raise NotImplementedError('subclass must implement interest()')
class SBI(bank):
    def interest(self):
        print('SBI interest rate: 6.5%')
class ICIC(bank):
    def interest(self):
        print('ICIC interest Rate: 5.5%')
class HDFC(bank):
    def interest(self):
        print('HDFC interest Rate: 5.2%')
banks = [SBI(),ICIC(),HDFC()]

for j in banks:
    j.interest()

'''






























