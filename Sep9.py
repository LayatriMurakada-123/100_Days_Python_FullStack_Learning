Python Project--> POP/OOP -->DSA(Logic based-->Pattern Based-->Platform Based)

POP(procedure  Oriented Programming)
-->Dividing the entire code into blocks --->Procedure -->functions(def)

Functions --> A Reusable block of code
          --> Block of Statements which performs a specific task
Syntax:

def <funcName>(paramerter):       #Function Definition
     """Doc String"""
     statements(s)....                   #function Body
     ................
     return value(s)

fname(args)  #function Call


Parameters-->These are like Formal Arguments
Arguments -->These are like excel arguments
Map--->Map is function which will map the inputs
if we take a,b it will became to inputs
or we take only a then it will take as collections



#Simple scenario to understand the functions

def add(a,b):
    """Addition Function"""
    return a+b
print(add(9,20))   #addition

c,d='codegnan','python'
print(add(c,d))   #Concatination

e,f=map(str,input("enter the values:").split(','))
print(add(e,f))

print(add([1,2,3],[4,5,6]))  #merging

print(add(1,2,3,4))    #Positinal arguments fail


#Variable length arguments --->*args
#-->we can pass any number of positional arguments
#-->where the data will be stored in tuple..()
#-->if we give a arguments in function like this (1,2,3,4,5)
#-->It will take it defaultly as a tuple

def sample(*a):
    """Demo of variable length Arguments"""
    print(a)
    print(type(a))
sample()    
sample(2,3,4,56,7)         #It will take defaultly as  a tuple
sample("likki",2,1.2,"codegnan",[89,9],2+5j)

marks=[20,30,40,50]
sample(marks)
sample(*marks)
# * is basically is used to unpacked the values into a collection

a,*b,c=12,'code','poll',2,4,9      # if we give like this outside function it will defaultly take as list
print(a)
print(b)
print(c)


def add(*a):
    """Perform addition for Numeric values"""
    print(a)
    result=0;
    for i in a:
        #if type(i)in [int,float]:
        #if type(i)==int or type(i)==float:
        if type(i) is int or type(i) is float:
            result+=i
    print(result)
        
add(1,2,3,4,5,6)

add(1,'s',9,'d',9.8)

#KerWord Arguments -->we can pass the name for the arguments
#First parameters should not be default but remain parameters we can take as default except first parameter
#Non default always follows a default arguments
#def batch(name="likki",age,place="vizag"):

def batch(name,age,place="vizag"):
    """Key Word Arguments Usage"""
    print(f'{name} is in {place} and age is{age} years')
batch("lavanya",20,"vizag")

batch(place='vizag',name='likki',age=22) #Keyword argumnets only needs name matching not order 

batch(name="likku",age=23)    #default arguments can accept a value as default

print(4,5)
print(4,5,sep=':')
# here keyword argument is sep and we are changing the default vlaue for sep

#Keyword variable length arguments (**Kwargs)
#-->Any number of keyword arguments ,data is stored in dictionary

def batch(**a):
    """Keyword Variable length arguments usage"""
    print(a)
    print(type(a))
batch()    
batch(name='lavanya',age=21,place="vizag")    

data={'name':['Akash','likki'],
      'place':['vizag','srikakulam']}

# batch(**data)
data.update({'batch':'PFS-VSP-004'})
batch(**data)

#task
Creat a function withe usage of *args & **Kwargs with real time secenrio
































    
