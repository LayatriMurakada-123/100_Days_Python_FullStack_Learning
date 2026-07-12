'''
        -: MODULES :-
           -------
---> A module is a python file (.py) that contains reusable code 

1.Variables
2.Functions
3.Classes
4.Objects
5.Statements

Why this :
--- ----
--> Instead of writing the same code repeatedly,we can store it in a module and use it whenever needed...
eg:-
---
import Module1
print(Module1.add(3,4))
print(Module1.exp(2,3))


Types of Modules:
----- -- -------

1.User-define :-
  ---- ------
--> import
eg:-
import Module1
print(Module1.add(3,4))
print(Module1.exp(2,3))

  

2.Built-in :-
  ----- --
--> math :
    ----
eg:-  
  import math
  print(math.sqrt(25))
  print(math.factorial(5))
  print(math.pow(2,3))
  print(math.pi)

  sqrt()       ---> square root
  factorial()  ---> factorial value
  pow()        ---> power
  ceil()       ---> roundup
  pi()         ---> pi value


--> OS :
    --
 ==> The Os module is used to interact with operating system
eg :-
import os
print(os.getcwd())
os.rmdir("module1")

 getcwd --> current directory
 mkdir  --> create folder


--> sys :
    ---
 ==> This will provide the information about python interpreter
 
 import sys
 print(sys.version)

--> random :
    ------
 ==> Used to generate random values
eg:
 import random
 print(random.randint(1000,9999))

 colors = ['yellow','red','blue','green']
 print(random.choice(colors))

'''

