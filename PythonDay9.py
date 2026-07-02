'''
      LOOPS
      -----

1.for loop   --> A for loop is used to iterate over a sequence ,list, tuple
  --- ----
    eg:-
    --   any_ = (1,2,3,4,5) #tuple
         for j in any_ :
               print(j)

         any_ = [1,2,3,4,5] #list
         for j in any_ :
              print(j)

        any_ = "python is a programming language"  #string
        for j in any_ :
             print(j)

        any_ = {"Name" : "Laya"
                 "Role" : "Trainee"}   #Dictionary
        for key in any_.values():
            print(key)

else in for loop :-
---- -- --- ----
--->  the else block will be executed after the for loop,but incase the loop is breaked then it will never entered in the else block

eg:-   any_ = [1,2,3,4,5]
       for val in any_ :
           print(val)
       else:
           print("program ended")

    
2.while loop   ---> the while loop will execute until the condition becomes true....
  ----- ----
   eg:-
   --   i = 1
        while i < 5:
             print(i)
             i += 1

'''





'''

                       "CONTROL STATEMENTS"
                        ------- ----------

1.break  ---> The break staatement is used to exit from the loop
  -----
  Eg:-
  ---   any_ = [1,2,3,4,5]
        for j in any_ :
            print(j)
            if j == 3:
                 break
        else:
            print("entered")
            

2.continue  ---> the continue will skip the current iteration
  --------
  eg:-
  --
   any_ = [1,2,3,4,5]
   for j in any_ :
      if j == 3:
           continue
      print(j)
   else:
      print("entered")
      

3.pass  ---> space holder
  ----
 eg:-
 --
   any_ = [1,2,3,4,5]
   for j in any_ :
       pass

range()---> range() is a in-built function that is used to generate a sequence upto a limit
------
    syntax --> range(start,end,step)
Ex:-
--  all_ = [1,2,3,4,5]
    for j in range(20):
         print(j)

assert keyword  ---> it will used to check the condition, but it will raise an error incase it is false...
------ -------
 eg:-
 --  
        age = int(input("Enter your age: "))
        assert age >= 18, "you must have 18 years"



'''

                
