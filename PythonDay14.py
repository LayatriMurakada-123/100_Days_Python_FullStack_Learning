'''
          -: Lambda Function :-
             ------ --------

--> This is also called as annonymous function..
--> A lambda function can take n number of arguments but having only one expression

syntax --> lambda arguments : expression

eg:-
--
S = lambda an , so , y : an * so - y
print(S(10,8,12))



filter()
--------
--> The filter() function is a built-in function used to filter elements from an iterables such as list , tuple and set based on condition

syntax --> filter(function , iterable)

--> This filter() function returns filter object so we can convert that into list , set and tuple
eg:-
---
nums = [1 , 2 , 3 ,  4 , 5]
rev = filter(lambda a: a%2 == 0,nums)
print(set(rev))

nums = [1 , 2 , 3 ,  4 , 5]
rev = filter(lambda a: a%2 != 0,nums)
print(set(rev))




                 -: LIST Comprehension :-
                    ---- -------------

---> This offers a shorter syntax when we want to create a new list from the old list

syntax --> variable_name = [expression loop condition]

eg:-
--
1.
old_ = [1,2,3,4,5,6]
new_ = [j for j in old_]
print(new_)

2.
old_ = [1,2,3,4,5,6]
new_ = [j for j in old_ if j % 2 != 0]
print(new_)




            -: Dictionary Comprehension :-
               ---------- -------------

---> This offers a shorter syntax when we want to create a new dict from the old dict

syntax --> variable_name = [expression loop]

eg:-
--
old_dict = {1:2 , 3:7 , 5:6}
new_dict = {i:j for (i,j) in old_dict.items() if j % 2 == 0}
print(new_dict)

'''













































