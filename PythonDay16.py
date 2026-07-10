'''
             -: GENERATORS :-
                ----------
---> This generator is special function that returns the iterator. Instead of returning all the values at once...
---> Here we are going to use yield keyword

eg:-
--
def S():
    yield 1
    yield 2
    yield 3
so = S()
print(next(so))
print(next(so))
print(next(so))


Working of Generator :-
------- -- ---------
---> When a function is called
---> It does not execute the function immediately...
---> It will returns the generator object
---> Then the fucntion will pauses at each yield...
---> when the next() is called again, execution resumes from where it stopped

eg-1:-
--
def demo():
    print("Start")
    yield 1

    print("Middle")
    yield 2

    print("End")
    yield 3
how = demo()
print(next(how))
print(next(how))
print(next(how))

eg-2:
-- -
def how(so):
    for i in range(so):
        yield i*i
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

#without generator
def sqrt(n):
    for i in range(n):
        print(i*i)
sqrt(5)


DIFFERNCES BETWEEN FUNCTIONS AND GENERATOR :-
---------- ------- --------- --- ---------

S.NO     FUNCTION                                    GENERATOR
----     --------                                    ---------
1.       Return                                      yield

2.       Return complete result                      Return one value at once

3.       Function will end after the return          Pauses after every yield
         the values

4.       More memory usage                           Less memory used

5.       Tis function never resume                   Resumes after next()


yield keyword:-
----- -------
--> This will produces the value
--> But the yield pauses the function
--> And yield will save the functions current state
--> yield will continues where it stopped...


next() keyword:-
------ -------
--> The next() function is used to retrieve the next value from a generator

eg:-
--
def how(S):
    for i in range(S):
        yield i*i
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))


Stop Iteration:-
----  ---------
--> Calling next() function after all values retrieve then it will raise Stop Iteration exception

eg:-
def how(S):
    for i in range(S):
        yield i*i
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

practice-1:
-------- -

def how(S):
    for i in range(S):
        yield i
any_ = how(10)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))



Generator expression:-
--------- ----------
---> The generator expression is similar to a list comprehension but uses parenthesis () instead of []

eg:-
--
gen = (X*X for X in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

'''





























