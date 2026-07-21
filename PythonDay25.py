'''
   -: Error Handling :-
      ===== ========

Syntax Error:-
------ -----

Ex:-
--
for j in range(1,10:
    print(j)

o/p -- SyntaxError


Indenttatation error:
-------------- -----

Ex:-
--
a = 20
for j in range(1,10)
    print(j)
else:
    print()

o/p -- IndentationError

Value Error:-
----- -----

Ex:-
--
num = int(input("Enter a num: "))

o/p -- ValueError




1. try:-
   ---
--> The try block will test the code for error

syntax -- try:

Ex:
--
try:
    print(num)
except:
    print('will get name error')



2. except:-
   ------
--> This except let us handle the errors in the code

syntax -- except:

Ex:-
--
1.
try:
    num = int(input("Enter a num: "))
except NameError:
    print('will get name error')

2.
try:
    num = int(input("Enter a num: "))
except ValueError:
    print('will get value error')

3.
try:
    num = int(input("Enter a num: "))
    num_2 = int(input("Enter a num: "))
    print(num/num_2)
except ZeroDivisionError:
    print('will get zerodivision error')
except ValueError:
    print('will get value error')

3. else:-
   ----
--> If the try block does not have any error then the else block will execute

Ex:-
--
try:
    num = int(input("Enter a num: "))
    num_2 = int(input("Enter a num: "))
    print(num/num_2)
except ZeroDivisionError:
    print('will get zerodivision error')
except ValueError:
    print('will get value error')

else:
    print("no error")
    

4. finally:-
   -------
-->  This block will execute whether the code is executed or has error.

Ex:-
--
try:
    num = int(input("Enter a num: "))
    num_2 = int(input("Enter a num: "))
    print(num/num_2)
except ZeroDivisionError:
    print('will get zerodivision error')
except ValueError:
    print('will get value error')
else:
    print("no error")
finally:
    print("end")


'''

