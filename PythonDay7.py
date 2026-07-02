'''
      INPUT FORMATTING FROM USER

input()
-------
--> The input() function is used to take input from user../

  1.int()
  -------
    ex:
    ---
      num = int(input("enter a number:"))
      num_2 = int(input("enter a number:"))
      print(num+num_2)

  2.string
  --------
    ex:
    ---
      how = input("enter a char:")
      print(how+'laya')

  3.float()
  --------
    ex:
    ---
      num = float(input("enter your salary:"))
      print(num,"is the monthly salary")

  4.list
  ------
    ex:
    ---
       group_ = list(map(int,input().split()))
       print(group_)

  5.tuple
  -------
   ex:-
   ---
     some = tuple(int,input().split()))
     print(some)

--> num = eval(input("Enter:"))
    print(type(num))

--> name_ = input("enter your name: ")
    age_ = int(input("enter your age:"))
    print(name_,"your age is",age_)
    print(f"{name_} your age is {age_}")  --->f string
    print("my name is %s and i'm %d years old" %(name_,age_))  ---> modulus string



  '''

name_ = input("enter your name: ")
age_ = int(input("enter your age:"))
print("my name is %s and i'm %d years old" %(name_,age_))


