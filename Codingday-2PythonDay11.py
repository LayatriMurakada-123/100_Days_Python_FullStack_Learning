'''
# 1.code for Palindrome program
so = input("Enter a word : ")
empty_ = ""
for j in so:
    empty_ = j + empty_
if empty_ == so:
    print(f"{so} is a palindrome")
else:
    print(f"{so} is not a palindrome")


# 2.code for fabinocci series
num = 0
num_2 = 1
limit_ = int(input("Enter a number : "))
print(num , num_2 , end = " ")
for i in range(1 , limit_+1):
    all_ = num + num_2
    num = num_2
    num_2 = all_
    print(all_ , end = " ")


# 3.code for calculator program
val_ = int(input("Enter number : "))
val_2 = int(input("Enter number : "))
user_in = int(input("Enter \n1.add \n2.sub \n3.mul \n4.pow : "))
if user_in == 1:
    print(val_ + val_2)
elif user_in == 2:
    print(val_ - val_2)
elif user_in == 3:
    print(val_ * val_2)
else:
    print(val_ ** val_2)


# 4.code for tables program
table_ = int(input("Enter a number : "))
for val in range(1,11):
    print(f"{table_} X {val} = {table_ * val}")



# 5.code for perfect number program
num = int(input("Enter a number : "))
sum_ = 0
for j in range(1,num):
    if num % j == 0:
        sum_ += j
if sum_ == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is a perfect number")
    
'''

    
