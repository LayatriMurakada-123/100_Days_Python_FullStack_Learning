'''
Passing by value :-
------- -- -----

def some(a):
    for j in a:
        print(j)
some([1,2,3])


return keyword :-
------ -------
--> In a function if a return is executed then it will exit from the function with certain returned values
eg:-
--
def myfunc_(b):
    return 5+b
a = myfunc_(10)
print(a)


Built-in functions:-
----- -- --------

code:-
----
import builtins

builtin_functions = [
    name for name in dir(builtins)
    if callable(getattr(builtins,name))]
print(builtin_functions)
print(f"Total built-in functions are {len(builtin_functions)}")
'''


'''
                     -: Recursive Function :-
                        --------- --------

---> Recursive function that calls itself repeatedly until a specified condition is met..

syntax
------
def fun_name(parameter):
    if condition:  -->base case
        return statement
    else:
        return statement
print(func_name(arguments))

eg:-
--
def func_name(num):
    if num == 1:
        return 1
    else:
        return num*func_name(num-1)
num = 10
print(func_name(num))

'''









