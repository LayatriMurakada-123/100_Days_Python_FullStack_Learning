'''
Self Keyword:-
---- -------
--> Self refers to current object...

Ex:-
--
class Test:
    def display(self):
        print(self)
te = Test()
print(te)
te.display()

Constructor:-
-----------
--> This constructor initializaes the object automatically when it is created...

Ex:-
--
class Batch:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
    def display(self):
        print(self.name)
        print(self.branch)
B4 = Batch('Laya','MCA')
B4.display()


Access Specifiers:-
------ ----------

Ex:-
--
#1.
class Batch:
    def __init__(self,name,branch):
        self._name = name
        self.branch = branch
    def display(self):
        print(self._name)
        print(self.branch)
B4 = Batch('Laya','MCA')
B4.display()



Protected:-
---------
class fam:
    def __init__(self):
        self._name = "Laya"
f = fam()
print(f._name)


Private:-
-------
#1.
class bank:
    def __init__(self):
        self.__pin = '6600'
AC = bank()
print(AC._bank__pin)


#2.
class bank:
    def __init__(self):
        self.__pin = '7700'
    def display(self):
        print(self.__pin)
ac = bank()
ac.display()


Encapsulation:-
-------------
--> Means wrapping the data and methods into a single unit(class) while controling access to the data

Ex:-
--
class atm:
    def __init__(self,balance):
        self._balance = balance
    def deposit(self,amount):
        self._balance += amount
        print(self._balance)
tran = atm(balance = int(input("Enter Amount: ")))
tran.deposit(amount = int(input("Enter Amount: ")))

'''

























