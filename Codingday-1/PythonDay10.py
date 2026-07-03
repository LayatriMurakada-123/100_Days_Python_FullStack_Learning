'''
# 1.Check prime or not prime single number
num = int(input("enter a number:"))
count = 0
for j in range(1,num+1):
    if num % j == 0:
        count += 1
if count == 2:
    print(f"{num} is a prime")
else:
    print(f"{num} is not a prime")

'''    

# 2.check prime or not in given  number
limit_ = int(input("enter a number : "))
for j in range(1,limit_+1):
    count = 0
    for i in range(1,j+1):
        if j % i == 0:
            count += 1
    if count == 2:
        print(f"{j} is a prime")
'''

# 3.print Right-angled triangle with '*'
num = 5
for j in range(1,num+1):
    for i in range(1,j+1):
        print("*", end = " ")
    print()

# 4.print Right-angled triangle with 'horizontal numbers'
num = 5
for j in range(1,num+1):
    for i in range(1,j+1):
        print(j, end = ' ')
    print()


# 5.print Right-angled triangle with 'vertical numbers'
num = 5
for j in range(1,num+1):
    for i in range(1,j+1):
        print(i, end = ' ')
    print()

# 6.print Right-angled triangle with 'non repeated numbers'
num = 5
count = 0
for j in range(1,num+1):
    for i in range(1,j+1):
        count +=1
        print(count, end = ' ')
    print()

# 7.print Right-angled triangle with 'non repeated numbers' in reverse
num = 4
count = 0
for j in range(num,0,-1):
    for i in range(1,j+1):
        count +=1
        print(count, end = ' ')
    print()

# 8.check whether number is amstrong number or not
am_str = int(input("enter a number : "))
length = len(str(am_str))
all_sum = 0
for j in str(am_str):
    all_sum += int(j) ** length
if all_sum == am_str:
    print(f"{am_str} is amstrong")
else:
    print(f"{am_str} is not amstrong")

# 9.Print a pyramid
num = 6
for j in range(num):
    print(" " *(num-j-1),end = " ")
    print("*" *(2*j+1))

'''





