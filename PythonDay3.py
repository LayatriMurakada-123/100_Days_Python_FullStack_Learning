'''
                                     -: DATATYPES :-
                                        ---------


int :-
---
num = 8


float :-
-----
num_2 = 7.89

ex:- num_2 = 7.89
     num = 6.89
     print(num//2)


String :-
------
--> String is a sequence of characters(char) that are enclosed in ' '," ",""" """
--> String is immutable

Concatination
-------------
--> Here, the (+) addition operator acts as to concatinate more then 2 strings...
   ex:-
      a = "python"
      b = "programming"
      print(a + b)


indexing :-
--------
--> This is used to access the particular char in the string by pass index position value...
--> Index start from 0......
--> We have negativi indexing to count the position from last to first....
   ex:-
     a = "python"
     print(a[2])
     print(a[-1])


Methods :-
-------
1.replace() --> This method is used to change any substring in that particular string...
            Syntax--> variable_name.replace("old string","new string",count)
            ex:-
               S = "python programming"
               print(S.replace("a","A"))
       
2.join() --> This method is used to add new substring after each char in the string...
         Sytax ---> "string".join(variable_name)
          ex:-
            S = "python"
            print("$".join(S))
            
3.split() --> This method can divide the string into different index into list, based on the string pass by us....
          Syntax --> variable_name.split('substring')
           ex:-
            S = "python is a language"
            print(so.split(" "))
            
4.count() --> This method is used to count the substring in the particular string and specify the index posistion...
           Syntax --> variable_name.count("substring",start index, ending index)
            ex:-
              S = "python is a language"
              print(S.count("a"))



String built-in function:-
------ ----- -- ----------

1.len()
  -----
     --> This will find the length of the string , which is number char present in that string
     ex:-
         S = "python"
         print(len(S))

2.max()
  -----
     --> This will be the max char in string
       ex:-
         S = "python"
         print(max(S))

3.min()
  -----
     --> this will be the min char in string
       ex:-
         S = "Python"
         print(min(S))

'''

time_ = "16.56"
parts_ = time_.split(":")
print("this time is",time_,"is convert into this",(parts_[0])-12,":",parts_[1])






