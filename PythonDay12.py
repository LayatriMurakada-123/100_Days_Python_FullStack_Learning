'''
        -: FUNCTIONS :-
           ---------
           
---> Function is a block of code that can be reusable
---> Function can avoid the repeated line of code...

Functions of 2 type:-
--------- -- - ----

1.buit-in functions:-
  ---- -- ---------
  eg--> print() , max() , type() , min() , sum()

2.user-define functions:-
  ---- ------ ---------
  --> This function starts with a keyword(def)

  def func_name(parameters):
      ------------
      ---------
      --------
  func_name(arguments)

  eg:-
  --- def add():
          print("hello!")
      add()

Types OF Arguments:-
----- -- ----------
1.Required arguments  --->  We have to pass same number of arguments with the definition of the function
      eg:-
      --    def add(a,b):
                print(a+b)
            add(2,3)

2.Default ---> 
         eg:-
         --
                num = 7
                num_2 = 9
                num_3 = 8
                def add(a,b,c):
                    print(a)
                    print(b)
                    print(c)
               add(num,num_2,num_3)

3.Keywords ---> We can pass as a pair like(variable = datatype)

4.variable length ---> Can pass n number of arguments  by using 'args' in the parameters , will receive tuple of argumentes and we can access those arguments by using indexing.
          eg:- -->(*args)
                num = 7
                num_2 = 9
                num_3 = 8
                def add(*a):
                    print(a)
                add(num,num_2,num_3)

        eg:-  -->(**asterisk)
        --       
              def all_(**Any_):
                  print(Any_['Age'])
              all_(Name = "Laya" , Age = 15)

              
a. LOCAL variable:- Defines inside a function and accessible only inside the functions
   ----- --------

b. Global variale:- Defines outside of the function and uses everywhere in the program
   ------ -------
 ---> This variable used throughout the program
           eg:-
               num = 9
               def func_():
                   print(num)
               func_()

note:-
----
  ---> To change the global variable by using keyword (global) that can change completely inside and outside of the function

  

Passing by value :-
------- -- -----

def some(a):
    for j in a:
        print(j)
some([1,2,3])

'''
